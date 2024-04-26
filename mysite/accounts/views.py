from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            User.objects.create_user(username=username, password=password)
            return redirect("events")
    return render(request, "accounts/register_user.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("events")
        else:
            print("Invalid User")
    return render(request, "accounts/login_user.html")


def logout_user(request):
    logout(request)
    return redirect("events")
