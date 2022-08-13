from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from onlinestore.views import context


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    users_list = context["users_list"]
    for logged_user in users_list:
        if username == logged_user["username"]:
            return render(request, "user_profile.html", logged_user)
    raise Http404("Немає такого користувача")


def login_view(request: HttpRequest) -> HttpResponse:
    """Login user view"""
    context = {}
    return render(request, "user_login.html", context)
