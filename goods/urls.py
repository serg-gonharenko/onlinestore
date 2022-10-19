from django.urls import path
from goods import views
from goods.views import ProductsListView, ProductsDetailView

app_name = "goods"
urlpatterns = [
    path("", ProductsListView.as_view(), name="list"),
    path("create/", views.products_create_view, name="create"),
    path("goods/<int:pk>/", ProductsDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", views.products_update_view, name="update"),
    path("<slug:slug>/delete/", views.products_delete_view, name="delete"),
]
