from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel


class CustomLoginView(LoginView):
    success_url = '/'
    template_name = 'users/user_login.html'

    def get_success_url(self):
        return self.success_url


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/user_register.html'
    success_url = '/'


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'


class CustomDetailView(LoginRequiredMixin, DetailView):
    model = CustomUserModel
    template_name = 'users/user_profile.html'


class CustomEditView(LoginRequiredMixin, UpdateView):
    model = CustomUserModel
    form_class = CustomUserChangeForm
    template_name = 'users/user_profile_edit.html'
    success_url = '/'

    def get_success_url(self):
        return self.success_url
