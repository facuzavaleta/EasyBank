from django.contrib import admin
from django.urls import path, include
from pages.views import about_view, contact_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('bankaccounts/', include("bankaccounts.urls")),
    path('transactions/', include("transactions.urls")),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('', home_view, name="home"),
]