# Generated by Django 3.2 on 2021-05-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymoney', '0005_alter_expense_expense_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mymoney.moneyaccount'),
        ),
        migrations.AlterField(
            model_name='income',
            name='income_note',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
