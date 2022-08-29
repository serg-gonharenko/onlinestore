from django.urls import path
from goods import views

app_name = "goods"
urlpatterns = [
    path("", views.products_list_view, name="list"),
    path("create/", views.products_create_view, name="create"),
    path("<slug:slug>/", views.products_detail_view, name="detail"),
    path("<slug:slug>/update/", views.products_update_view, name="update"),
    path("<slug:slug>/delete/", views.products_delete_view, name="delete"),
]
