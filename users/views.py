from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


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
