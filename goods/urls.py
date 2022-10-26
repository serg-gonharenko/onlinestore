from django.urls import path
from goods import views
from goods.views import ProductsListView, ProductsDetailView, ProductsUpdateView,\
    ProductsCreateView, ProductsDeleteView

app_name = "goods"
urlpatterns = [
    path("", ProductsListView.as_view(), name="list"),
    path("goods/<int:pk>/", ProductsDetailView.as_view(), name="detail"),
    path("goods/update/<int:pk>/", ProductsUpdateView.as_view(), name="update"),
    path("goods/create/", ProductsCreateView.as_view(), name="create"),
    path("goods/delete/<int:pk>/", ProductsDeleteView.as_view(), name="delete"),
]
