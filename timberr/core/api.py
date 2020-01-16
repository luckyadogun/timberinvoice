from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRegistrationAPIView, LoginAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
]