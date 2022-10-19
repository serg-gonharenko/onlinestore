from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from goods.models import Products, Categories
from goods.forms import ProductsForm
from django.urls import reverse
from django.views.generic import ListView, DetailView


class ProductsListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products


def products_list_view(request: HttpRequest) -> HttpResponse:
    cont = Products.objects.all()
    context = {"object_list": Products.objects.all()}
    return render(request, "goods/products_list.html", context)


def products_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        context = {"object": Products.objects.get(slug=slug)}
        return render(request, "goods/products_detail.html", context)
    except Products.DoesNotExist:
        raise Http404("Немає такого товару")


def products_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            redirect_url = form.instance.get_absolute_url()
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProductsForm()

    return render(request, "goods/products_form.html", {"form": form})


def products_update_view(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        instance = Products.objects.get(slug=slug)
    except Products.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = ProductsForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            redirect_url = form.instance.get_absolute_url()
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProductsForm(instance=instance)

    return render(request, "goods/products_form.html", {"form": form})


def products_delete_view(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        instance = Products.objects.get(slug=slug)
    except Products.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        instance.delete()
        redirect_url = reverse("goods:list")
        return HttpResponseRedirect(redirect_url)

    return render(
        request, "goods/products_confirm_delete.html", {"object": instance}
    )
