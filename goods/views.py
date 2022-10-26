from goods.models import Products, Categories
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    paginate_by = 4
    model = Products


class ProductsDetailView(DetailView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    fields = '__all__'
    success_url = '/'


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    fields = '__all__'
    success_url = '/'


class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = "goods/products_confirm_delete.html"
    success_url = '/'
