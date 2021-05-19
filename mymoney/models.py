from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MoneyAccount(models.Model):
    account_user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    account_number = models.IntegerField(null=True, blank=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name = "Account"


class Expense(models.Model):
    expense_user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_date = models.DateTimeField()
    expense_category = models.CharField(max_length=100)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_description = models.CharField(max_length=350)
    expense_note = models.CharField(max_length=350, blank=True)
    expense_account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.expense_amount) + " - for " + self. expense_description

    def save(self, *args, **kwargs):
        self.expense_account.account_balance -= int(self.expense_amount)
        self.expense_account.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.expense_account.account_balance += self.expense_amount
        self.expense_account.save()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Expense"


class Income(models.Model):
    income_user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_date = models.DateTimeField()
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_description = models.CharField(max_length=350)
    income_note = models.CharField(max_length=350, null=True, blank=True)
    income_account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.income_amount) + " from " + self.income_description

    def save(self, *args, **kwargs):
        innit_balance = self.income_amount
        #Created is a logic to specify ONLY if object is new
        created = not self.pk
        if created :
            self.income_account.account_balance += int(self.income_amount)
            self.income_account.save()
        else:
            account_chaenge = innit_balance
           
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.income_account.account_balance -= self.income_amount
        self.income_account.save()
        super(self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Income"



class Transfers(models.Model):
    transfer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField()
    transfer_from = models.ForeignKey(MoneyAccount,  related_name='transfer_from', on_delete=models.CASCADE)
    transfer_to = models.ForeignKey(MoneyAccount, related_name='transfer_to', on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(max_digits=10, decimal_places = 2)
    transfer_reason = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.transfer_amount) + " transferred"

    def save(self, *args, **kwargs):
        self.transfer_to.account_balance += int(self.transfer_amount)
        self.transfer_from.account_balance -= int(self.transfer_amount)
        self.transfer_from.save()
        self.transfer_to.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.transfer_to.account_balance -= self.transfer_amount
        self.transfer_from.account_balance += self.transfer_amount
        self.transfer_from.save()
        self.transfer_to.save()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Transfers"

class ToBePaid(models.Model):
    tobe_user = models.ForeignKey(User, on_delete=models.CASCADE)
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