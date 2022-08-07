import datetime

from django.db import models
import datetime


def get_default_date() -> datetime.date:
    return datetime.datetime.now().date()


class Client(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    created_at = models.DateField(auto_created=True, default=get_default_date)
    updated_at = models.DateField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
