from rest_framework import routers, viewsets
from django.contrib.auth.models import User
from . import serializers, models

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.MoneyAccount.objects.all()
    serializer_class = serializers.AccountSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

