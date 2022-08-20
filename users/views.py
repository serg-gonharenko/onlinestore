from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm


def user_profile(request: HttpRequest) -> HttpResponse:
    """User profile view"""
    if request.user.is_authenticated:
        return render(request, "user_profile.html")
    return HttpResponseRedirect(reverse_lazy("login"))


def login_view(request: HttpRequest) -> HttpResponse:
    """Login user view"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse_lazy("homepage"))
    else:
        form = LoginForm()

    return render(request, "user_login.html", {'form': form})


def register_view(request: HttpRequest) -> HttpResponse:
    """ Register new user view """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.create_user()
            redirect_url = reverse("login")
            return HttpResponseRedirect(redirect_url)
    else:
        form = RegisterForm()

    return render(request, "user_register.html", {'form': form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
