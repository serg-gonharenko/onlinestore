""" Users App URL Configuration"""

from django.urls import path
from users.views import user_profile, login_view, logout_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("profile/", user_profile, name="user_profile"),
    path("logout/", logout_view, name="logout"),

]