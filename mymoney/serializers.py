from django.db.models import fields
from rest_framework import serializers
from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyAccount
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyAccount
        fields = '__all__'

class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transfers
        fields = '__all__'