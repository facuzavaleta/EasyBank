# Generated by Django 4.1.3 on 2022-12-29 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0035_alter_bankaccount_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 17, 48, 44, 497398)),
        ),
    ]
