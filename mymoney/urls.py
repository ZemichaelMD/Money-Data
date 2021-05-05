from django.urls import path
from . import views


urlpatterns = [
    path('', views.ExpenceListView.as_view(), name='index'),
    path('expenses', views.ExpenceListView.as_view(), name='expenses'),
    path('income', views.IncomeListView.as_view(), name='incomes'),
    path('transfers', views.TransferListView.as_view(), name='transfers'),
    path('accounts', views.AccountListView.as_view(), name='accounts'),

    path('expenses/update/<int:pk>', views.ExpenceUpdateView.as_view(), name='expense_update'),
    path('income/update/<int:pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('transfers/update/<int:pk>', views.TransfersUpdateView.as_view(), name='transfers_update'),
    path('accounts/update/<int:pk>', views.AccountsUpdateView.as_view(), name='accounts_update'),
    path('newexpense', views.ExpensesCreateView.as_view(), name='create_expense'),
]