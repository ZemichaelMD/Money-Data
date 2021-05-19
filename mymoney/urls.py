from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('adddata/', views.addFromExel, name="addfromexel"),

    path('', views.AccountListView.as_view(), name='index'),
    path('expenses', views.ExpenceListView.as_view(), name='expenses'),
    path('income', views.IncomeListView.as_view(), name='incomes'),
    path('transfers', views.TransferListView.as_view(), name='transfers'),
    path('accounts', views.AccountListView.as_view(), name='accounts'),

    path('expenses/update/<int:pk>', views.ExpenceUpdateView.as_view(), name='expense_update'),
    path('income/update/<int:pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('transfers/update/<int:pk>', views.TransfersUpdateView.as_view(), name='transfers_update'),
    path('accounts/update/<int:pk>', views.AccountsUpdateView.as_view(), name='accounts_update'),

    path('expenses/delete/<int:pk>', views.ExpenseDeleteView.as_view(), name='expense_update'),

    path('newexpense', views.ExpensesCreateView.as_view(), name='create_expense'),
    path('newincome', views.IncomeCreateView.as_view(), name='create_income'),
    path('newtransfer', views.TransferCreateView.as_view(), name='create_transfer'),
    path('account', views.AccountCreateView.as_view(), name='create_account'),

    path('syncexpence', views.syncExpense, name='SyncE'),

    path('login', views.CostomLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(next_page = 'login'), name='logout'),

    path('api/', views.apiOverview, name='api-response'),
    path('api/task-list/', views.expenseList, name='api-response'),

]