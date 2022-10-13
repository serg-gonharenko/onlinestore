"""
Users application forms
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    print("Creation form")

    class Meta:
        model = CustomUserModel
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUserModel
        fields = ("username", "email")