from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserRegistrationAPIView, LoginAPIView,
    ClientViewset, InvoiceViewset)

router = DefaultRouter()
router.register(r"client", viewset=ClientViewset, base_name="client")
router.register(r"invoice", viewset=InvoiceViewset, base_name="invoice")

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
]

urlpatterns += router.urls