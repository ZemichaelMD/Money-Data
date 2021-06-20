from . import models
from mymoney import serializers
from .serializers import AccountSerializer, ExpenseSerializer

#REST API
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'Account List': '127.0.0.1:8000/account_list/',
        'Account Create': '127.0.0.1:8000/account_create/',
        'Account Detail': '127.0.0.1:8000/account_detail/<int:pk>/',
        'Account Update': '127.0.0.1:8000/account_update/<int:pk>/',
        'Account Delete': '127.0.0.1:8000/account_delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def expenseList(request):
    expenses = models.Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True,)
    return Response(serializer.data)


@api_view(['GET'])
def accountList(request):
    accounts = models.MoneyAccount.objects.all()
    serializer = AccountSerializer(accounts, many = True,)
    return Response(serializer.data)


@api_view(['GET'])
def incomeList(request):
    accounts = models.MoneyAccount.objects.all()
    serializer = AccountSerializer(accounts, many = True,)
    return Response(serializer.data)


@api_view(['GET'])
def transfersList(request):
    accounts = models.MoneyAccount.objects.all()
    serializer = AccountSerializer(accounts, many = True,)
    return Response(serializer.data)
