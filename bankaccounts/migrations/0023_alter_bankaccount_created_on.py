# Generated by Django 4.1.3 on 2022-11-26 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0022_alter_bankaccount_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 3, 8, 48, 505237)),
        ),
    ]
