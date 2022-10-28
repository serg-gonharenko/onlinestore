from django.urls import path
from .views import CustomLoginView,\
    CustomLogoutView, CustomRegisterView, CustomDetailView, CustomEditView, CustomDeleteView

app_name = 'users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', CustomDetailView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', CustomEditView.as_view(), name='edit'),
    path('profile/delete/<int:pk>/', CustomDeleteView.as_view(), name='delete'),
]
