from django.db import models
from bankaccounts.models import BankAccount
from datetime import datetime
TYPE_CHOICES = (("Deposit", "Deposit"), ("Extraction", "Extraction"), ("Transference", "Transference"), ("Exchange", "Exchange"))

# Create your models here.
class Transference(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    sender = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    receiver = models.CharField(max_length=50, null=True)

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

class Extraction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

class Exchange(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    sender = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="receiver", null=True)

class HistorialObject(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="accountS", null=True)
    accountReceiver = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="accountReceiver", null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transactiontype = models.CharField(max_length=12, choices=TYPE_CHOICES)
    created_on = models.DateTimeField(default=datetime.now())

class HistorialObjectReceived(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="accountR", null=True)
    accountSender = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="accountSender", null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transactiontype = models.CharField(max_length=12, choices=TYPE_CHOICES)
    created_on = models.DateTimeField(default=datetime.now())