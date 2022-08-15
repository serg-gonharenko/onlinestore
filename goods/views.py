from typing import Dict, Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from goods.models import Products, Categories

# Create your views here.


def all_products_list_view(request: HttpRequest) -> dict[str, Any]:
    return {
        "products_list": Products.objects.all()
    }


def product_about(request: HttpRequest, product_slug) -> HttpResponse:
    try:
        context = {
            "object": Products.objects.get(slug=product_slug)
        }
        return render(request, "product_about.html", context)
    except:
        raise Http404("Немає такого товару")
