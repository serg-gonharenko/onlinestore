from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from onlinestore.views import context
# Create your views here.


def product_about(request: HttpRequest, product_slug) -> HttpResponse:
    show_prod = [x for x in context["goods_list"] if x["slug"] == product_slug]
    show_prod_dict = {"title": show_prod[0]["product"], "data": show_prod[0]}
    return render(request, "product_about.html", show_prod_dict)
