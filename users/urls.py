""" Users App URL Configuration"""

from django.urls import path
from users.views import user_profile, login_view, logout_view, register_view


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("profile/", user_profile, name="user_profile"),
    path("logout/", logout_view, name="logout"),

]