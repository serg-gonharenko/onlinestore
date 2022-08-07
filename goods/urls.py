from django.urls import path
from goods.views import product_about

urlpatterns = [
    path('<slug:product_slug>/', product_about, name='product_about_url'),
        ]