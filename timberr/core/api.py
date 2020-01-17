from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .views import (UserRegistrationAPIView, LoginAPIView,
    ClientViewset, InvoiceViewset)


# endpoints
list_create_client = ClientViewset.as_view({"get": "list", "post": "create"})
retrieve_delete_client = ClientViewset.as_view({"get": "retrieve", "delete": "destroy"})

list_create_invoice = InvoiceViewset.as_view({"get": "list", "post": "create"})
retrieve_delete_invoice = InvoiceViewset.as_view({"get": "retrieve", "delete": "destroy"})
update_invoice = InvoiceViewset.as_view({"put": "update_invoice"})

# URI

urlpatterns = [
    path(
        "docs",
        include_docs_urls(
            title="Timberr API", authentication_classes=[], permission_classes=[]
        ),
    ),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('client/', list_create_client, name="list-create-client"),
    path('client/<int:pk>/', retrieve_delete_client, name="client-detail"),
    path('invoice/', list_create_invoice, name="list-create-invoice"),
    path('invoice/<int:pk>/', retrieve_delete_invoice, name="invoice-detail"),
    path('invoice/<int:pk>/update', update_invoice, name="update-invoice"),

]
