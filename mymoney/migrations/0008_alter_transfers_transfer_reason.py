# Generated by Django 3.2 on 2021-05-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoney', '0007_transfers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='transfer_reason',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]