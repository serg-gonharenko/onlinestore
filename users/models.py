"""
User application models
"""


from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """Custom user model"""

    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"
