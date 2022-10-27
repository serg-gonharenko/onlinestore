from django.contrib import admin
from goods.models import Categories, Products

admin.site.register(Categories)
# admin.site.register(Products)


class ProductsAdmin(admin.ModelAdmin):
    """Класс для кастомизации модели на панели админа"""

    list_display = "code", "name", "price", "quantity",
    list_display_links = "name",
    list_editable = "price", "quantity"
    list_filter = "price", "quantity"


admin.site.register(Products, ProductsAdmin)
