from django.urls import path, include
from rest_framework import routers

from . import views, viewSets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', viewSets.UserViewSet)
router.register(r'accounts', viewSets.AccountViewSet)
router.register(r'expenses', viewSets.ExpenseViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.apiOverview, name='api-response'),
    path('api/', views.apiOverview, name='api-response'),

    path('api/accounts/', views.accountList, name='account_list'),
    path('api/expenses/', views.expenseList, name='expenses_list'),
    path('api/incomes/', views.incomeList, name='income_list'),
    path('api/transfers/', views.transfersList, name='transfers_list'),

]