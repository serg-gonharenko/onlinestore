from django.db import models
import datetime


def get_default_date() -> datetime.date:
    return datetime.datetime.now().date()


class Categories(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    created_at = models.DateField(auto_created=True, default=get_default_date)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"


class Products(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    created_at = models.DateField(auto_created=True, default=get_default_date)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
