from django.shortcuts import render
from .forms import DepositForm, ExtractionForm, TransferenceForm, ExchangeForm
from bankaccounts.models import BankAccount
from .models import HistorialObject, HistorialObjectReceived
from decimal import Decimal
from django.contrib.auth.models import User
from uuid import UUID
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

#Functions
def checkIsPositive(amount):
    if amount > 0:
        return False
    else:
        return True

def checkMaxLimit(amount):
    if amount > 9999999999:
        return True

def checkBalanceExceeded(amount):
    if amount > 9999999999:
        return True

def checkSameAccount(sender, receiver):
    if sender.account_number == receiver.account_number:
        return True

def checkSameCurrency(sender, receiver):
    if sender.currency == receiver.currency:
        return True

def checkUUID(receiver):
    try:
        UUID(receiver)
        return True
    except:
        return False

# Create your views here.
def transactions_index(request):
    return render(request, 'transactions_index.html', {})

def transactions_deposit(request):
    form = DepositForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_deposit.html', context)

def transactions_depositsave(request):
    form = DepositForm(request.POST)
    bankaccount = BankAccount.objects.get(account_number=request.POST["account"])
    amount = request.POST["amount"]
    amount = Decimal(amount)

    if checkIsPositive(amount):
        return render(request, "transactions_depositnegativenumber.html", {})

    elif checkMaxLimit(amount):
        return render(request, "transactions_depositexceeded.html", {})

    elif checkBalanceExceeded(bankaccount.balance + amount):
        return render(request, "transactions_depositbalanceexceeded.html", {})

    else:
        bankaccount.balance += amount

    bankaccount.save()

    receipt = HistorialObject(
        account = bankaccount,
        amount = amount,
        transactiontype = "Deposit"
    )
    receipt.save()

    context = {
        "bankaccount": bankaccount,
        "receipt": receipt,
    }

    # import pdb; pdb.set_trace()

    if form.is_valid():
        form.save()
        return render(request, 'transactions_depositsuccess.html', context)
    else:
        return render(request, 'transactions_depositsuccess.html', context)

def transactions_depositsavedownloadPDF(request):
    receipt = HistorialObject.objects.last()

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 800, f"                                                             ©EasyBank")

    p.drawString(50, 750, f"Receipt N°: {receipt.id}")
    p.drawString(50, 725, f"Type: {receipt.transactiontype}")
    p.drawString(50, 700, f"Account: {receipt.account.account_number}")
    p.drawString(50, 675, f"Bank: {receipt.account.bank}")
    p.drawString(50, 650, f"Currency: {receipt.account.currency}")
    p.drawString(50, 625, f"Amount: +${receipt.amount}")
    p.drawString(50, 600, f"Date: {str(receipt.created_on)[:19]}")
    p.drawString(50, 575, f"Balance: ${receipt.account.balance}")

    p.line(18,550,580,550) 


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'receipt' + str(receipt.id) + '.pdf')

def transactions_extraction(request):
    form = ExtractionForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_extraction.html', context)

def transactions_extractionsave(request):
    form = ExtractionForm(request.POST)
    bankaccount = BankAccount.objects.get(account_number=request.POST["account"])
    amount = request.POST["amount"]
    amount = Decimal(amount)
    extractionLimit = None

    context = {
        "bankaccount": bankaccount,
        "amount": amount,
    }
    if checkIsPositive(amount):
        return render(request, "transactions_extractionnegativenumber.html", {})
        
    elif amount <= bankaccount.balance:
        bankaccount.balance -= amount
        bankaccount.save()

        receipt = HistorialObject(
            account = bankaccount,
            amount = amount,
            transactiontype = "Extraction")
        receipt.save()

        context = {
            "bankaccount": bankaccount,
            "amount": amount,
            "receipt": receipt,
        }
        
        if form.is_valid():
            form.save()
            return render(request, 'transactions_extractionsuccess.html', context)
        else:
            return render(request, 'transactions_extractionsuccess.html', context)
        
    else:
        return render(request, 'transactions_extractionfail.html', context)

def transactions_extractionsavedownloadPDF(request):
    receipt = HistorialObject.objects.last()

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 800, f"                                                             ©EasyBank")

    p.drawString(50, 750, f"Receipt N°: {receipt.id}")
    p.drawString(50, 725, f"Type: {receipt.transactiontype}")
    p.drawString(50, 700, f"Account: {receipt.account.account_number}")
    p.drawString(50, 675, f"Bank: {receipt.account.bank}")
    p.drawString(50, 650, f"Currency: {receipt.account.currency}")
    p.drawString(50, 625, f"Amount: -${receipt.amount}")
    p.drawString(50, 600, f"Date: {str(receipt.created_on)[:19]}")
    p.drawString(50, 575, f"Balance: ${receipt.account.balance}")

    p.line(18,550,580,550) 


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'receipt' + str(receipt.id) + '.pdf')

def transactions_exchange(request):
    form = ExchangeForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_exchange.html', context)

def transactions_exchangesave(request):
    form = ExchangeForm(request.POST)
    sender = BankAccount.objects.get(account_number=request.POST["sender"])
    receiver = BankAccount.objects.get(account_number=request.POST["receiver"])
    amount = request.POST["amount"]
    amount = Decimal(amount)
    conversion = 300

    context = {
    "form": form,
    "sender": sender,
    "receiver": receiver,
    "amount": amount,
    }

    if checkSameAccount(sender, receiver):
        return render(request, 'transactions_exchangesamenumber.html', context)

    elif checkSameCurrency(sender, receiver):
        return render(request, 'transactions_exchangesamecurrency.html', context)
    
    elif checkIsPositive(amount):
        return render(request,"transactions_exchangenegativenumber.html", context)

    elif amount > sender.balance:
        return render(request, 'transactions_exchangefail.html', context)

    elif checkBalanceExceeded(Decimal(receiver.balance) + amount):
        return render(request, 'transactions_exchangebalanceexceeded.html', context)

    elif amount <= sender.balance:
        if sender.currency == "ARS" and receiver.currency == "USD":
            sender.balance -= amount
            receiver.balance += amount / conversion
            converted = amount / conversion
            sender.save()
            receiver.save()

            receipt = HistorialObject(
                account = sender,
                accountReceiver = receiver,
                amount = amount,
                transactiontype = "Exchange")
            receipt.save()

            receiptReceiver = HistorialObjectReceived(
                account = receiver,
                accountSender = sender,
                amount = converted,
                transactiontype = "Exchange")
            receiptReceiver.save()

            context = {
                "form": form,
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "receipt": receipt,
                "receiptReceiver": receiptReceiver,
                "conversion": conversion,
                "converted": converted,
            }

            if form.is_valid():
                form.save()
                return render(request, 'transactions_exchangesuccess.html', context)
            else:
                return render(request, 'transactions_exchangesuccess.html', context)
        
        elif sender.currency == "USD" and receiver.currency == "ARS":
            sender.balance -= amount
            receiver.balance += amount * conversion
            converted = amount * conversion
            sender.save()
            receiver.save()

            receipt = HistorialObject(
                account = sender,
                accountReceiver = receiver, 
                amount = amount,
                transactiontype = "Exchange")
            receipt.save()

            receiptReceiver = HistorialObjectReceived(
                account = receiver,
                accountSender = sender,
                amount = converted,
                transactiontype = "Exchange")
            receiptReceiver.save()

            context = {
                "form": form,
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "receipt": receipt,
                "receiptReceiver": receiptReceiver,
                "conversion": conversion,
                "converted": converted,
            }
            
            if form.is_valid():
                form.save()
                return render(request, 'transactions_exchangesuccess.html', context)
            else:
                return render(request, 'transactions_exchangesuccess.html', context)

def transactions_exchangesavedownloadPDF(request):
    receipt = HistorialObject.objects.last()

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 800, f"                                                             ©EasyBank")

    p.drawString(50, 750, f"Receipt N°: {receipt.id}")
    p.drawString(50, 725, f"Type: {receipt.transactiontype}")
    p.drawString(50, 700, f"Sender: {receipt.account.account_number}")
    p.drawString(50, 675, f"Bank: {receipt.account.bank}")
    p.drawString(50, 650, f"Currency: {receipt.account.currency}")
    p.drawString(50, 625, f"Amount: -${receipt.amount}")
    p.drawString(50, 600, f"Receiver: {receipt.accountReceiver.account_number}")
    p.drawString(50, 575, f"Bank: {receipt.accountReceiver.bank}")
    p.drawString(50, 550, f"Currency: {receipt.accountReceiver.currency}")    
    p.drawString(50, 525, f"Date: {str(receipt.created_on)[:19]}")
    p.drawString(50, 500, f"Balance Sender: ${receipt.account.balance}")
    p.drawString(50, 475, f"Balance Receiver: ${receipt.accountReceiver.balance}")

    p.line(18,450,580,450) 


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'receipt' + str(receipt.id) + '.pdf')

def transactions_transference(request):
    form = TransferenceForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_transference.html', context)

def transactions_transferencesave(request):
    try:
        form = TransferenceForm(request.POST)
        sender = BankAccount.objects.get(account_number=request.POST["sender"])
        receiver = BankAccount.objects.get(account_number=request.POST["receiver"])
        amount = request.POST["amount"]
        amount = Decimal(amount)

        context = {
            "form": form,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
        }

        if checkSameAccount(sender, receiver):
            return render(request, 'transactions_transferencesamenumber.html', context)

        elif not checkSameCurrency(sender, receiver):
            return render(request, 'transactions_transferencesamecurrency.html', context)

        elif checkIsPositive(amount):
            return render(request, 'transactions_transferencenegativenumber.html', {})

        elif amount > sender.balance:
            return render(request, 'transactions_transferencefail.html', context)

        elif checkBalanceExceeded(receiver.balance + amount):
            return render(request, 'transactions_transferencebalanceexceeded.html', {})

        elif amount <= sender.balance:
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()

            receipt = HistorialObject(
                account = sender,
                accountReceiver = receiver, 
                amount = amount,
                transactiontype = "Transference")
            receipt.save()

            receiptReceiver = HistorialObjectReceived(
                account = receiver,
                accountSender = sender,
                amount = amount,
                transactiontype = "Transference")
            receiptReceiver.save()

            context = {
            "form": form,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "receipt": receipt,
            "receiptReceiver": receiptReceiver
            }

            if form.is_valid():
                form.save()
                return render(request, 'transactions_transferencesuccess.html', context)
            else:
                return render(request, 'transactions_transferencesuccess.html', context)
    except:
        return render(request, 'transactions_transferenceuuid.html', {})

def transactions_transferencesavedownloadPDF(request):
    receipt = HistorialObject.objects.last()

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 800, f"                                                             ©EasyBank")

    p.drawString(50, 750, f"Receipt N°: {receipt.id}")
    p.drawString(50, 725, f"Type: {receipt.transactiontype}")
    p.drawString(50, 700, f"Sender: {receipt.account.account_number}")
    p.drawString(50, 675, f"Bank: {receipt.account.bank}")
    p.drawString(50, 650, f"Currency: {receipt.account.currency}")
    p.drawString(50, 625, f"Amount: -${receipt.amount}")
    p.drawString(50, 600, f"Receiver: {receipt.accountReceiver.account_number}")
    p.drawString(50, 575, f"Bank: {receipt.accountReceiver.bank}")
    p.drawString(50, 550, f"Date: {str(receipt.created_on)[:19]}")
    p.drawString(50, 525, f"Balance Sender: ${receipt.account.balance}")

    p.line(18,500,580,500) 


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'receipt' + str(receipt.id) + '.pdf')