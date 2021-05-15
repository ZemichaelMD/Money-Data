# Generated by Django 3.2.2 on 2021-05-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoney', '0013_auto_20210507_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='expense_synced',
        ),
        migrations.RemoveField(
            model_name='income',
            name='income_synced',
        ),
        migrations.RemoveField(
            model_name='transfers',
            name='transfer_synced',
        ),
        migrations.AlterField(
            model_name='moneyaccount',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
