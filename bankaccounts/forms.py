from django import forms
from django.contrib.auth.models import User
from .models import BankAccount
from django.db import models

CURRENCY_CHOICES = (("ARS", "ARS"), ("USD", "USD"))
BANK_CHOICES = (("BANCO NACION", "BANCO NACION"), ("BANCO SANTANDER", "BANCO SANTANDER"), ("BANCO GALICIA", "BANCO GALICIA"))

class BankAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BankAccountForm, self).__init__(*args, **kwargs)
        self.fields['balance'].widget.attrs.update({'placeholder': 'Initial account balance'})

    class Meta:
        model = BankAccount
        exclude = ("user", "created_on",)