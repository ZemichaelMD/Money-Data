from django.shortcuts import render
from django.http import HttpResponse
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

class TransferListView(ListView):
    model = models.Transfers
    template_name = "mymoney/transfers_list.html"

class AccountListView(ListView):
    model = models.MoneyAccount
    template_name = "mymoney/accounts_list.html"

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



class ExpensesCreateView(CreateView):
    model = models.Expense
    fields = '__all__'
    template_name = "mymoney/new_expense.html"