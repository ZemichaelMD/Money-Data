from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView,DetailView, UpdateView,CreateView

from . import models

# Create your views here.
#class based Listviews
class ExpenceListView(ListView):
    model = models.Expense
    template_name = "mymoney/expense_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Expence Data"
        return context

class IncomeListView(ListView):
    model = models.Income
    template_name = "mymoney/income_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Income Data"
        return context

class TransferListView(ListView):
    model = models.Transfers
    template_name = "mymoney/transfers_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Transfer Data"
        return context

class AccountListView(ListView):
    model = models.MoneyAccount
    template_name = "mymoney/accounts_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Accounts Data"
        return context

#class based DetailViews
class ExpenceUpdateView(UpdateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

class IncomeUpdateView(UpdateView):
    model = models.Income
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

class TransfersUpdateView(UpdateView):
    model = models.Transfers
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

class AccountsUpdateView(UpdateView):
    model = models.MoneyAccount
    fields = '__all__'
    template_name = "mymoney/generic_update_view.html"

    def get_success_url(self):
        view_name = 'index'
        # No need for reverse_lazy here, because it's called inside the method
        return reverse(view_name)


class ExpensesCreateView(CreateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/new_expense.html"

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
