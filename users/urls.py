""" Users App URL Configuration"""

from django.urls import path
from users.views import login_view, logout_view, register_view, user_profile_edit_view, user_profile_view

app_name = "users"
urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("profile/edit", user_profile_edit_view, name="profile_edit"),
    path("profile/", user_profile_view, name="user_profile"),
    path("logout/", logout_view, name="logout"),


]