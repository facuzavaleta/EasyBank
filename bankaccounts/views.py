from django.shortcuts import render, redirect
from .forms import BankAccountForm
from .models import BankAccount
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from transactions.models import HistorialObject, HistorialObjectReceived

# Create your views here.
def bankaccounts_index(request):
    bankaccounts = BankAccount.objects.filter(user__id=request.user.id)
    context = {
        'bankaccounts': bankaccounts,
    }
    return render(request, 'bankaccounts_index.html', context)

def bankaccounts_create(request):
    context = {
        'form': BankAccountForm()
    }
    return render(request, 'bankaccounts_create.html', context)

def bankaccounts_createsave(request):
    form = BankAccountForm(request.POST)

    balance = int(request.POST["balance"])

    if balance > 9999999999:
        return render(request, "bankaccounts_balanceexceeded.html", {})

    elif balance < 0:
        return render(request, "bankaccounts_negativenumber.html", {})

    elif form.is_valid():
        instance = form.save(commit=False)
        instance.user = User.objects.get(id=request.user.id)
        instance.save()
        return HttpResponseRedirect(reverse("bankaccounts_index"))
    else:
        return HttpResponseRedirect(reverse("bankaccounts_index"))

def bankaccounts_detail(request, account_number):
    bankaccount = BankAccount.objects.get(account_number=account_number)
    historialObjects = HistorialObject.objects.filter(account=bankaccount).order_by("-created_on").values()
    conversion = 300
    context = {
        'bankaccount': bankaccount,
        'historialObjects': historialObjects,
        'conversion': conversion,
    }
    return render(request, 'bankaccounts_detail.html', context)

def bankaccounts_movements(request, account_number):
    bankaccount = BankAccount.objects.get(account_number=account_number)
    historialObjects = HistorialObject.objects.filter(account=bankaccount).order_by("-created_on").values()
    historialObjectsReceived = HistorialObjectReceived.objects.filter(account=bankaccount).order_by("-created_on").values()
    conversion = 300
    context = {
        'bankaccount': bankaccount,
        'historialObjects': historialObjects,
        'historialObjectsReceived': historialObjectsReceived,
        'conversion': conversion,
    }
    return render(request, 'bankaccounts_movements.html', context)

def bankaccounts_delete(request, account_number):
    return render(request, 'bankaccounts_deleteconfirmation.html', {})

def bankaccounts_deleteConfirmation(request, account_number):
    bankaccount = BankAccount.objects.get(account_number=account_number)
    bankaccount.delete()
    return HttpResponseRedirect(reverse("bankaccounts_index"))