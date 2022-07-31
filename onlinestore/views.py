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
    ],
}


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
