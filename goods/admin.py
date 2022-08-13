from django.contrib import admin
from goods.models import Categories, Products

admin.site.register(Categories)


class ProductsAdmin(admin.ModelAdmin):
    list_display = "slug", "name", "price", "quantity"
    list_display_links = "name",
    list_editable = "price", "quantity"
    list_filter = "price", "quantity"



admin.site.register(Products, ProductsAdmin)
