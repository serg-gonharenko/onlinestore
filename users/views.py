from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from onlinestore.views import context


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    users_list = context["users_list"]
    for user in users_list:
        if username == user["username"]:
            return render(request, "user_profile.html", context)
    return HttpResponseNotFound("Немає такого користувача")

