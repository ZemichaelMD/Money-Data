from django.contrib import admin
from .models import Expense, Income, MoneyAccount, ToBePaid

# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(MoneyAccount)
admin.site.register(ToBePaid)
