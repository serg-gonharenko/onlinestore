from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from goods.views import all_products_list_view
context = {
    "users_list": [
        {
            "id": 1,
            "username": "shorodilov",
            "first_name": "Serhii",
            "last_name": "Horodilov"
        },
        {
            "id": 2,
            "username": "serhhoncharenko",
            "first_name": "Serhii",
            "last_name": "Honcharenko"
        },
    ],
}
# TODO: вынести проверку пользователя в отдельную фунцию check_user и добавить в контекст страниц только словать или
#  на следующей домашке сделать как положено через Логин


def homepage(request: HttpRequest) -> HttpResponse:
    current_user = "serhhoncharenko"
    users_list = context["users_list"]
    qs = all_products_list_view(request)
    for registered_user in users_list:
        if current_user == registered_user["username"]:
            home_context = {"username": current_user}
            home_context.update(qs)
            return render(request, "homepage.html", home_context)
    home_context = {"username": "Anonimus"}
    home_context.update(qs)
    return render(request, "homepage.html", home_context)


def about(request: HttpRequest) -> HttpResponse:
    current_user = "serhhoncharenko"
    users_list = context["users_list"]
    for registered_user in users_list:
        if current_user == registered_user["username"]:
            about_context = {"username": current_user}
            return render(request, "about.html", about_context)
    about_context = {"username": "Anonimus"}
    return render(request, "about.html", about_context)


