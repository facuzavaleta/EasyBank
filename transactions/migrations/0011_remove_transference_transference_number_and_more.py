# Generated by Django 4.1.3 on 2022-11-25 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_alter_historialobject_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transference',
            name='transference_number',
        ),
        migrations.AlterField(
            model_name='historialobject',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 25, 17, 0, 56, 242630)),
        ),
    ]
