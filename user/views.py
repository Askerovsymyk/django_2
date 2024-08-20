

from django.shortcuts import render, redirect
from user.forms import UserRegisterForm, LoginRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register_view(request):
    if request.method == "GET":
        form = UserRegisterForm()
        return render(request=request, template_name="user/register.html", context={"form": form})
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            return render(request=request, template_name="user/register.html", context={"form": form})
        User.objects.create_user(
            username=form.cleaned_data["username"],
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            password=form.cleaned_data["password"])
        return redirect("/")


def login_view(request):
    if request.method == "GET":
        form = LoginRegisterForm()
        return render(request=request, template_name="user/login.html", context={"form": form})

    if request.method == "POST":
        form = LoginRegisterForm(request.POST)
        if not form.is_valid():
            return render(request=request, template_name="user/login.html", context={"form": form})
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if not user:
            form.add_error(None, "wrong username or password")
            return render(request=request, template_name="user/login.html", context={"form": form})
        login(request, user)
        return redirect("/")

def logout_view(request):
    logout(request)
    return redirect("/")









