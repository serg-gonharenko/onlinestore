"""
Users application forms
"""

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from users.models import UserModel


class RegisterForm(forms.Form):
    """Form for registering new user"""
    username = forms.CharField(max_length=64, label="Ім'я користувача")
    email = forms.EmailField(label="email")
    password1 = forms.CharField(
        max_length=255, label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        max_length=255, label="Підтвердити пароль", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("User already exists")
        except UserModel.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError("Passwords missmatch")

    def create_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        UserModel.objects.create_user(username, email, password)


class LoginForm(forms.Form):
    """Form for login user"""
    username = forms.CharField(max_length=64, label="Ім'я користувача")
    password = forms.CharField(
        max_length=255, label="Пароль", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self.user = authenticate(username=username, password=password)

        if self.user is None:
            message = "Неправильні ім'я користувача або пароль"
            raise ValidationError(message)


class ProfileEdit(forms.Form):
    """Form for edit User data"""

    first_name = forms.CharField(max_length=64, label="Ім'я")
    last_name = forms.CharField(max_length=64, label="Прізвище")
    email = forms.EmailField(label="email")

    def save(self, user):
        UserModel.objects.filter(pk=user.pk).update(**self.cleaned_data)
