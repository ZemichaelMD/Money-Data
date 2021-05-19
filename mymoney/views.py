from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, UpdateView,CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from .serializers import ExpenseSerializer

from datetimewidget.widgets import DateTimeWidget

from . import models

# Create your views here.
# Class based Listviews
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


# Class based UpdateViews
class ExpenceUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/generic_update.html"

    success_url = reverse_lazy("expenses")


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Income
    fields = '__all__'
    template_name = "mymoney/generic_update.html"

    success_url = reverse_lazy('incomes')


class TransfersUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Transfers
    fields = '__all__'
    template_name = "mymoney/generic_update.html"

    success_url = reverse_lazy('transfers')


class AccountsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.MoneyAccount
    fields = ['account_name','account_number', 'account_balance']
    template_name = "mymoney/generic_update.html"

    success_url = reverse_lazy('accounts')


# Class based CreateViews
class AccountCreateView(LoginRequiredMixin, CreateView):
    model = models.MoneyAccount
    fields = ['account_name','account_number', 'account_balance']
    template_name = "mymoney/generic_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccountCreateView, self).form_valid(form)

    success_url = reverse_lazy("accounts")


class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = models.Expense
    fields = ['expense_date','expense_category','expense_amount','expense_description','expense_note','expense_account']
    template_name = "mymoney/generic_create.html"

    def get_form(self, *args, **kwargs):
        # Add date picker in forms
        from .widgets import XDSoftDateTimePickerInput
        # Django's own Datetime Selector
        from django.forms.widgets import SelectDateWidget
        #Django Admin DatePicker
        from django.contrib.admin.widgets import AdminDateWidget
        form = super(ExpensesCreateView, self).get_form()
        form.fields['expense_date'].widget = SelectDateWidget()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExpensesCreateView, self).form_valid(form)

    success_url = reverse_lazy("expenses")


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = models.Income
    fields = ['income_date','income_amount', 'income_description', 'income_note','income_account',]
    template_name = "mymoney/generic_create.html"

    def get_form(self, *args, **kwargs):
        from django.forms.widgets import SelectDateWidget
        form = super(IncomeCreateView, self).get_form()
        form.fields['income_date'].widget = SelectDateWidget()
        return form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncomeCreateView, self).form_valid(form)

    success_url = reverse_lazy("incomes")


class TransferCreateView(LoginRequiredMixin, CreateView):
    model = models.Transfers
    fields = ['transfer_date', 'transfer_from', 'transfer_to', 'transfer_amount', 'transfer_reason']
    template_name = "mymoney/generic_create.html"

    def get_form(self, *args, **kwargs):
        from django.forms.widgets import SelectDateWidget
        form = super(TransferCreateView, self).get_form()
        form.fields['transfer_date'].widget = SelectDateWidget()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransferCreateView, self).form_valid(form)

    success_url = reverse_lazy("transfers")

#Class based DeleteViews
class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/generic_delete.html"

    success_url = reverse_lazy("expenses")

class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Income
    fields = '__all__'
    template_name = "mymoney/generic_delete.html"

    success_url = reverse_lazy("incomes")

class TransferDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Transfers
    fields = '__all__'
    template_name = "mymoney/generic_delete.html"

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

def addFromExel(request):
    import xlrd
    import datetime
    from .models import Expense
    from django.contrib.auth.models import User
    me = User.objects.get(username="zee")

    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'templates\mymoney\MoneyData.xls')
    book = xlrd.open_workbook(file_path)

    added_data = []

    #Adding Expences
    sheet_expence = book.sheet_by_name('Expences')

    # printing how many rows the workbook has
    # print(sheet.nrows)

    for i in range(sheet_expence.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_expence.row_values(i)

        #print each Row
        #print(row_header_set)

        # print nested cells
        # for cell in row:
        # print (cell)

        # This returns the pure data!!
        try:
            #Grabbing Date
            date = int(row_header_set[0])
            #convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))

            #Datetime Converter to Django Date time
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware

            exexpence_date_formated = make_aware(date_as_datetime)

            #Add Expence
            my_expence_account = models.MoneyAccount.objects.filter(account_name="Cash")

            models.Expense.objects.create(expense_user = me, expense_date = exexpence_date_formated, expense_category=str(row_header_set[1]),
                         expense_amount=float(row_header_set[2]), expense_description=str(row_header_set[3]),
                         expense_note=str(row_header_set[4]),expense_account=my_expence_account[0])
            print("done adding Expence" + str(row_header_set[3]))
            added_data.append("done adding Expence :" + str(row_header_set[3]))

        except Exception as e:
            print("Adding Expense failed!")
            print(e)
            pass

    #Adding Income
    sheet_income = book.sheet_by_name('Income')

    # printing how many rows the workbook has
    print(sheet_income.nrows)

    for j in range(sheet_income.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_income.row_values(j)

        # print each Row
        #print(row_header_set)

        # print nested cells
        # for cell in row:
        # print (cell)

        # This returns the pure data!!
        try:
            # Grabbing Date
            date = int(row_header_set[0])
            # convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))


            # Datetime Converter to Django Date time
            from django.utils.timezone import make_aware
            expence_date_formated = make_aware(date_as_datetime)

            # Add income
            my_income_account = models.MoneyAccount.objects.filter(account_name=str(row_header_set[1]))

            models.Income.objects.create(income_user = me, income_date=expence_date_formated, income_amount=float(row_header_set[2]),
                              income_description=str(row_header_set[3]),income_account=my_income_account[0])
            print("done adding" + str(row_header_set[3]))
            added_data.append("done adding Income :" + str(row_header_set[3]))

        except Exception as e:
            print(e)
            pass

    #Adding Transfers
    sheet_transfers = book.sheet_by_name('Transfers')

    # printing how many rows the workbook has
    print(sheet_transfers.nrows)

    for k in range(sheet_transfers.nrows):
        # row_header_set contains all the data as a set
        row_header_set = sheet_transfers.row_values(k)

        # print each Row
        #print(row_header_set)

        # print nested cells
        # for cell in row:
        # print (cell)

        # This returns the pure data!!
        try:
            # Grabbing Date
            date = int(row_header_set[0])
            # convert exel Date to Python
            date_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode))

            # Datetime Converter to Django Date time
            import datetime
            from django.conf import settings
            from django.utils.timezone import make_aware

            exexpence_date_formated = make_aware(date_as_datetime)

            # Add Transfer
            transferedfrom = models.MoneyAccount.objects.filter(account_name=str(row_header_set[1]))
            transferedto = models.MoneyAccount.objects.filter(account_name=str(row_header_set[2]))

            #print(str(row_header_set[3])+' From : '+transferedfrom[0].account_name+' to: '+transferedto[0].account_name)
            #print(exexpence_date_formated)
            models.Transfers.objects.create(transfer_user = me , transfer_date=exexpence_date_formated,
                                            transfer_from=transferedfrom[0],
                                            transfer_to=transferedto[0],
                                            transfer_amount=float(row_header_set[3]),
                                            transfer_reason=str(row_header_set[4]))
            print('done!')
            added_data.append("done adding Transfer :" + str(row_header_set[3])+' From : '+transferedfrom[0].account_name+' to: '+transferedto[0].account_name)
        except Exception as e:
            print(e)
            pass

    print ("Done adding...")
    context = {'added_data': added_data}
    return render(request, 'mymoney/excel.html', context)

#REST API
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'Account List': '/account_list/',
        'Account Create': '/account_create/',
        'Account Detail': '/account_detail/<int:pk>/',
        'Account Update': '/account_update/<int:pk>/',
        'Account Delete': '/account_delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def expenseList(request):
    expenses = models.Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True,)
    return Response(serializer.data)
