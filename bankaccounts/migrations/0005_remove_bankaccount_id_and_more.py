# Generated by Django 4.1.3 on 2022-11-22 15:30

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0004_bankaccount_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='id',
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 12, 30, 55, 709218)),
        ),
    ]
