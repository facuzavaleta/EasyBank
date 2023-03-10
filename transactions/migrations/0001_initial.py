# Generated by Django 4.1.3 on 2022-11-10 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankaccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.BigIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.bankaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.bankaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit_Extraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('option', models.CharField(choices=[('SENT', 'SENT'), ('RECEIVED', 'RECEIVED')], max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.bankaccount')),
            ],
        ),
    ]
