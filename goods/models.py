from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Categories(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    product_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"


class Products(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    product_img = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("goods:detail", kwargs={"slug": self.slug})
