# Generated by Django 4.1.3 on 2022-11-26 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0022_alter_historialobject_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialobject',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 3, 23, 15, 186214)),
        ),
    ]
