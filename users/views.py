from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    context = {}
    return render(request, "user_profile.html", context)
