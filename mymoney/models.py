from django.db import models


# Create your models here.
class ToBePaid(models.Model):
    tobe_date = models.DateTimeField()
    tobe_from = models.CharField(max_length=100)
    tobe_work = models.CharField(max_length=300)
    tobe_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tobe_Sure = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tobe_amount) + " from " + self.tobe_from

    class Meta:
        verbose_name = "To Be Paid"
        verbose_name_plural = "To Be Paid"


class MoneyAccount(models.Model):
    account_name = models.CharField(max_length=100)
    account_number = models.IntegerField(null=True, blank=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name = "Account"


class Expense(models.Model):
    expense_date = models.DateTimeField()
    expense_category = models.CharField(max_length=100)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_description = models.CharField(max_length=350)
    expense_note = models.CharField(max_length=350, blank=True)
    expense_account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.expense_amount) + " - for " + self. expense_description

    class Meta:
        verbose_name = "Expense"


class Income(models.Model):
    income_date = models.DateTimeField()
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_description = models.CharField(max_length=350)
    income_note = models.CharField(max_length=350, null=True, blank=True)
    income_account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.income_amount) + " from " + self.income_description

    class Meta:
        verbose_name = "Income"


'''class Transfers(models.Model):
    transfer_date = models.DateTimeField()
    transfer_from = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE)
    transfer_to = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(max_digits=10, decimal_places = 2)
    transfer_reason = models.CharField(max_length=300)

    def __str__(self):
        return str(self.transfer_amount) + " transferred"

    class Meta:
        verbose_name = "Transfers" '''
