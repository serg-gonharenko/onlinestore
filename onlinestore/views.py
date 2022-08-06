from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

context = {
    "goods_list": [
        {
            "id": 1,
            "product": "Canon E500",
            "slug": "canon-e500",
            "available": False,
            "description": "some product description",
            "price": 50000.00,
        },
        {
            "id": 2,
            "product": "Sony A7III",
            "slug": "sony-a7iii",
            "available": True,
            "description": "some product description",
            "price": 75999.99
        },
    ],
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


def homepage(request: HttpRequest) -> HttpResponse:
    current_user = "serhhoncharenko"
    users_list = context["users_list"]
    for registered_user in users_list:
        if current_user == registered_user["username"]:
            home_context = {"goods_list": context["goods_list"],
                            "username": current_user}
            return render(request, "homepage.html", home_context)
    home_context = {"goods_list": context["goods_list"],
                        "username": "Anonimus"}
    return render(request, "homepage.html", home_context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


