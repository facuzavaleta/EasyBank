from django import forms
from django.contrib.auth.models import User
from .models import BankAccount
from django.db import models

CURRENCY_CHOICES = (("ARS", "ARS"), ("USD", "USD"))
BANK_CHOICES = (("BANCO NACION", "BANCO NACION"), ("BANCO SANTANDER", "BANCO SANTANDER"), ("BANCO GALICIA", "BANCO GALICIA"))

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        exclude = ("user", "created_on",)