from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.bankaccounts_index, name="bankaccounts_index"),
    path("create/", views.bankaccounts_create, name="bankaccounts_create"),
    path("create/createsave/", views.bankaccounts_createsave, name="bankaccounts_createsave"),
    path("<str:account_number>/", views.bankaccounts_detail, name="bankaccounts_detail"),
    path("<str:account_number>/delete/", views.bankaccounts_delete, name="bankaccounts_delete"),
    path("<str:account_number>/movements/", views.bankaccounts_movements, name="bankaccounts_delete"),
    path("<str:account_number>/delete/delete/", views.bankaccounts_deleteConfirmation, name="bankaccounts_deleteConfirmation"),

    
]