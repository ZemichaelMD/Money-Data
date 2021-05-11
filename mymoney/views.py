from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, UpdateView,CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from .serializers import ExpenseSerializer

from . import models

# Create your views here.
#class based Listviews
class CostomLoginView(LoginView):
    template_name = "mymoney/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class ExpenceListView(LoginRequiredMixin, ListView):
    model = models.Expense
    template_name = "mymoney/expense_list.html"
    context_object_name = "expenses"

    def get_queryset(self):
        return models.Expense.objects.order_by('-expense_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = context['expenses'].filter(expense_user=self.request.user)
        context['count'] = context['expenses'].filter(expense_user=self.request.user).count
        context["page_title"] = "Expence Data"
        return context

class IncomeListView(LoginRequiredMixin, ListView):
    model = models.Income
    template_name = "mymoney/income_list.html"
    context_object_name = 'incomes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = context['incomes'].filter(income_user=self.request.user)
        context["page_title"] = "Income Data"
        return context

class TransferListView(LoginRequiredMixin, ListView):
    model = models.Transfers
    template_name = "mymoney/transfers_list.html"
    context_object_name = 'transfers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transfers'] = context['transfers'].filter(transfer_user=self.request.user)
        context["page_title"] = "Transfer Data"
        return context

class AccountListView(LoginRequiredMixin, ListView):
    model = models.MoneyAccount
    template_name = "mymoney/accounts_list.html"
    context_object_name = 'accounts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = context['accounts'].filter(account_user=self.request.user)
        context["page_title"] = "Accounts Data"
        return context

#class based UpdateViews
class ExpenceUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

    success_url = reverse_lazy("expenses")

class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Income
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

    success_url = reverse_lazy('incomes')

class TransfersUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Transfers
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

    success_url = reverse_lazy('transfers')

class AccountsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.MoneyAccount
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

    success_url = reverse_lazy('accounts')

#Class based CreateViews
class AccountCreateView(LoginRequiredMixin, CreateView):
    model = models.MoneyAccount
    fields = '__all__'
    template_name = "mymoney/new_expense.html"

    success_url = reverse_lazy("accounts")


class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/new_expense.html"

    success_url = reverse_lazy("expenses")


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = models.Income
    fields = '__all__'
    template_name = "mymoney/new_expense.html"

    success_url = reverse_lazy("incomes")


class TransferCreateView(LoginRequiredMixin, CreateView):
    model = models.Transfers
    fields = '__all__'
    template_name = "mymoney/new_expense.html"

    success_url = reverse_lazy("transfers")



def syncExpense(request):
    context = {}
    expenseslist = models.Expense.objects.all()
    incomelist = models.Income.objects.all()
    transferslist = models.Transfers.objects.all()

    for expense in expenseslist:
        if expense.expense_synced == False :
            exaccount = expense.expense_account
            examount = expense.expense_amount
            exaccount.account_balance -= examount
            exaccount.save()
            expense.expense_synced = True
            expense.save()
            print("Done Sync" + expense.expense_description)
            context["Done"] = 'Done Syncing' + str(expense.expense_description)

        for income in incomelist:
            if income.income_synced == False:
                inaccount = income.income_account
                inamount = income.income_amount
                inaccount.account_balance += inamount
                inaccount.save()
                income.income_synced = True
                income.save()
                print("Done Sync" + income.income_description)
                context["Done"] = 'Done Syncing' + str(income.income_description)

        for transfer in transferslist:

            if transfer.transfer_synced == False:
                transferfrom = transfer.transfer_from
                transferto = transfer.transfer_to
                transferamount = transfer.transfer_amount

                transferfrom.account_balance -= transferamount
                transferto.account_balance += transferamount

                transferfrom.save()
                transferto.save()

                transfer.transfer_synced = True
                transfer.save()
                print("Done Sync" + transfer.transfer_reason)
                context["Done"] = 'Done Syncing' + str(transfer.transfer_reason)

    return render(request, 'mymoney/syncexisting.html', context = context)


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'Account List':'/account_list/',
        'Account Create': '/account_create/',
        'Account Detail':'/account_detail/<int:pk>/',
        'Account Update': '/account_update/<int:pk>/',
        'Account Delete': '/account_delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def expenseList(request):
    expenses = models.Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True,)

    return Response(serializer.data)