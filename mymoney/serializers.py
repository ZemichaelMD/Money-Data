from rest_framework import serializers
from . import models


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyAccount
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyAccount
        fields = '__all__'