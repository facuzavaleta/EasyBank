# Generated by Django 4.1.3 on 2023-01-03 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0039_alter_bankaccount_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 5, 16, 50, 595377)),
        ),
    ]
