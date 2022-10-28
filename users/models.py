"""
User application models
"""


from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    """Custom users model"""

    class Meta:
        db_table = "auth_user"
        verbose_name = "users"
        verbose_name_plural = "users"
