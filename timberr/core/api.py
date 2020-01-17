from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserRegistrationAPIView, LoginAPIView,
    ClientViewset, InvoiceViewset)

list_create_client = ClientViewset.as_view({"get": "list", "post": "create"})
retrieve_delete_client = ClientViewset.as_view({"get": "retrieve", "delete": "destroy"})

list_create_invoice = InvoiceViewset.as_view({"get": "list", "post": "create"})
retrieve_delete_invoice = InvoiceViewset.as_view({"get": "retrieve", "delete": "destroy"})
update_invoice = InvoiceViewset.as_view({"put": "update_invoice"})


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('client/', list_create_client, name="list-create-client"),
    path('client/<int:pk>/', retrieve_delete_client, name="client-detail"),
    path('invoice/', list_create_invoice, name="list-create-invoice"),
    path('invoice/<int:pk>/', retrieve_delete_invoice, name="invoice-detail"),
    path('invoice/<int:pk>/update', update_invoice, name="update-invoice"),

]
