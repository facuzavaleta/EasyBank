from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def users_index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users_index.html', context)

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, "register_fail.html", {})
