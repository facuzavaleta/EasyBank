# Generated by Django 4.1.3 on 2022-11-11 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0003_alter_bankaccount_user'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Transference',
        ),
        migrations.RenameField(
            model_name='transference',
            old_name='transaction_number',
            new_name='transference_number',
        ),
    ]
