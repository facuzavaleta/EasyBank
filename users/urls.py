from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("", views.users_index, name="users_index"),
]