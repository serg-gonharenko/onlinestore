from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_profile(request: HttpRequest) -> HttpResponse:
    """User profile view"""
    if request.user.is_authenticated:
        return render(request, "user_profile.html")
    return HttpResponseRedirect(reverse_lazy("login"))


def login_view(request: HttpRequest) -> HttpResponse:
    """Login user view"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse_lazy("login"))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy("homepage"))
    return render(request, "user_login.html")


def register_view(request: HttpRequest) ->HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]

        if User.objects.filter(username=username):
            return HttpResponseRedirect(reverse_lazy("register"))

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            User.objects.create_user(username=username, password=password1)
            return HttpResponseRedirect(reverse_lazy("login"))

        return HttpResponseRedirect(reverse_lazy("register"))

    return render(request, "user_register.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
