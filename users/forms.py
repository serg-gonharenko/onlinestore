"""
Users application forms
"""

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from users.models import UserModel


class RegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(label="Pass1", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Pass2", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        user_model = get_user_model()
        try:
            user_model.objects.get(username=username)
            self.add_error("username", " user already exists")
        except user_model.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        # user_model = get_user_model()
        if password1 and password2 and password1 != password2:
            self.add_error("password1", "Passwords missmatch")

    def create_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data.get('password1')
        email = self.cleaned_data.get('email')
        UserModel.objects.create_user(username, email, password)


class ProfileEditModelForm(forms.ModelForm):
    """Form for edit User data"""
    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email")

    def save(self):
        pass
        UserModel.objects.filter(pk=user.pk).update(**self.cleaned_data)


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        # fields = "__all__"
        fields = ("username", "password")
        widgets = {"password": forms.PasswordInput()}
        labels = {"username": "Ім'я користувача",
                  "password": "Пароль"
                  }
        help_texts = {'username': None}

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
