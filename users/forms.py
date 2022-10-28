"""
Users application forms
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUserModel
        fields = ("username", "email", "first_name", "last_name",)
