from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from onlinestore.views import context

# TODO переписать user_profile
def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    users_list = context["users_list"]
    for logged_user in users_list:
        if username == logged_user["username"]:
            return render(request, "user_profile.html", logged_user)
    raise Http404("Немає такого користувача")


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
