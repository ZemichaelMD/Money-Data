# Generated by Django 3.2 on 2021-04-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoney', '0002_auto_20210426_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyaccount',
            name='account_number',
            field=models.IntegerField(null=True),
        ),
    ]
