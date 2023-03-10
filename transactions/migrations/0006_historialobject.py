# Generated by Django 4.1.3 on 2022-11-23 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_transference_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transactiontype', models.CharField(choices=[('Deposit', 'Deposit'), ('Extraction', 'Extraction'), ('Transference', 'Transference'), ('Exchange', 'Exchange')], max_length=12)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 7, 48, 19194))),
            ],
        ),
    ]
