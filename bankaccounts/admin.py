from django.contrib import admin
from bankaccounts.models import BankAccount
# Register your models here.
class BankAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(BankAccount, BankAccountAdmin)