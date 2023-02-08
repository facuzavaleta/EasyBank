from django import forms
from .models import Deposit, Extraction, Transference, Exchange
from bankaccounts.models import BankAccount
from django.contrib.auth.models import User

class DepositForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extraer el request pasado desde el form
        self.request = kwargs.pop("request", None)
        super(DepositForm, self).__init__(*args, **kwargs)
        # Por defecto el queryset debe estar vacio
        self.fields["account"].queryset = BankAccount.objects.none()
        if self.request:
            if self.request.user.is_authenticated:
                # si el request no es vacio y el usuario esta logeado, obtener el id del usuario y filtrar el queryset
                self.fields["account"].queryset = BankAccount.objects.filter(user__id=self.request.user.id)
                
    class Meta:
        model = Deposit
        fields = "__all__"

class ExtractionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extraer el request pasado desde el form
        self.request = kwargs.pop("request", None)
        super(ExtractionForm, self).__init__(*args, **kwargs)
        # Por defecto el queryset debe estar vacio
        self.fields["account"].queryset = BankAccount.objects.none()
        if self.request:
            if self.request.user.is_authenticated:
                # si el request no es vacio y el usuario esta logeado, obtener el id del usuario y filtrar el queryset
                self.fields["account"].queryset = BankAccount.objects.filter(user__id=self.request.user.id)

    class Meta:
        model = Extraction
        fields = "__all__"

class TransferenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extraer el request pasado desde el form
        self.request = kwargs.pop("request", None)
        super(TransferenceForm, self).__init__(*args, **kwargs)
        # Por defecto el queryset debe estar vacio
        self.fields["sender"].queryset = BankAccount.objects.none()
        if self.request:
            if self.request.user.is_authenticated:
                # si el request no es vacio y el usuario esta logeado, obtener el id del usuario y filtrar el 
                self.fields["sender"].queryset = BankAccount.objects.filter(user__id=self.request.user.id)

    class Meta:
        model = Transference
        exclude = ("transference_number",)

class ExchangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extraer el request pasado desde el form
        self.request = kwargs.pop("request", None)
        super(ExchangeForm, self).__init__(*args, **kwargs)
        # Por defecto el queryset debe estar vacio
        self.fields["sender"].queryset = BankAccount.objects.none()
        if self.request:
            if self.request.user.is_authenticated:
                # si el request no es vacio y el usuario esta logeado, obtener el id del usuario y filtrar el queryset
                self.fields["sender"].queryset = BankAccount.objects.filter(user__id=self.request.user.id)
        self.fields["receiver"].queryset = BankAccount.objects.none()
        if self.request:
            if self.request.user.is_authenticated:
                # si el request no es vacio y el usuario esta logeado, obtener el id del usuario y filtrar el queryset
                self.fields["receiver"].queryset = BankAccount.objects.filter(user__id=self.request.user.id)

    class Meta:
        model = Exchange
        fields = "__all__"