""" Users App URL Configuration"""

from django.urls import path
from users.views import user_profile


urlpatterns = [
    path('<str:username>/', user_profile, name="user_profile"),
]