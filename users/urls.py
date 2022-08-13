""" Users App URL Configuration"""

from django.urls import path
from users.views import user_profile, login_view


urlpatterns = [
    path("", login_view, name="login"),
    path('<str:username>/', user_profile, name="user_profile"),

]