from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from goods.views import all_products_list_view


def homepage(request: HttpRequest) -> HttpResponse:
    home_context = all_products_list_view(request)
    return render(request, "homepage.html", home_context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


