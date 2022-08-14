from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


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


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
