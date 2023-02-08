from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
# Create your models here.
CURRENCY_CHOICES = (("ARS", "ARS"), ("USD", "USD"))
BANK_CHOICES = (("ICBC", "ICBC"),("BANCO NACION", "BANCO NACION"), ("BANCO SANTANDER", "BANCO SANTANDER"), ("BANCO GALICIA", "BANCO GALICIA"))

class BankAccount(models.Model):
    account_number = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=20, choices=BANK_CHOICES)
    created_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.user) + "-" + self.currency + "-" + str(self.account_number)