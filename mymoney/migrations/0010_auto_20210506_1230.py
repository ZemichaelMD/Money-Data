# Generated by Django 3.2 on 2021-05-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoney', '0009_auto_20210504_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_synced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='income',
            name='income_synced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transfers',
            name='transfer_synced',
            field=models.BooleanField(default=False),
        ),
    ]