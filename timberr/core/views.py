from datetime import timedelta
import datetime
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, views, viewsets
from .models import User, Client, Invoice

# auth_backend
from .auth_backend import CustomAuthBackend
authenticate = CustomAuthBackend.authenticate

# pagination
from .pagination import CustomCursorPagination

from .serializers import (RegistrationSerializer, 
    ClientSerializer, LoginSerializer, InvoiceSerializer)

import jwt
import jsend


class UserRegistrationAPIView(generics.CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class LoginAPIView(views.APIView):
    """
    APIView to handle user Authentication.
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = request.data.get('email')
            password = request.data.get('password')

            if email and password != "":
                if self.queryset.filter(email=email).exists():
                    user = self.queryset.get(email=email)
                    is_password = check_password(password, user.password)

                    if is_password:
                        authenticate(self, request, email=user.email, password=user.password)

                        if user.is_active:
                            login(request, user)

                            payload = {
                                "id": user.id, 
                                "email": user.email, 
                                "exp": datetime.datetime.utcnow()
                                        + timedelta(seconds=604800)
                                }
                            return Response(
                                jsend.success(
                                    {
                                        "token": jwt.encode(payload, settings.SECRET_KEY),
                                        "user": serializer.data
                                    }
                                ),
                                status=status.HTTP_201_CREATED,
                            )
                        else:
                            return Response(
                                (jsend.error("Account is inactive")),
                                status=status.HTTP_403_FORBIDDEN,
                            )
                    else:
                        return Response(
                            (jsend.error("'password' : ['Incorrect password']")),
                            status=status.HTTP_401_UNAUTHORIZED,
                        )
                else:
                    return Response(
                        (jsend.error("email or password does not match")),
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            else:
                return Response(
                    (
                        jsend.fail(
                            {
                                "email": ["Email is required"],
                                "password": ["Password is required"],
                            }
                        )
                    ),
                    status=status.HTTP_400_BAD_REQUEST,
                )
        

class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomCursorPagination

    def list(self, request):
        queryset = self.queryset.filter(created_by=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(
                jsend.success({"client": serializer.data}),
                status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(
                jsend.success({"client": serializer.data}), 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                jsend.error("INVALID REQUEST"), 
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            jsend.success({"client": serializer.data}),
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            jsend.success({"client": "Successfully Deleted"}),
            status=status.HTTP_200_OK)

    @action(detail=False)
    def get_total_client(self, request):
        total_clients = Client.objects.count()
        return Response(
                    jsend.success({"client": {"total": total_clients}}),
                    status=status.HTTP_200_OK,
                )
    


class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomCursorPagination

    def list(self, request):
        queryset = self.queryset.filter(created_by=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(
                jsend.success({"invoice": serializer.data}),
                status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(
                jsend.success({"invoice": serializer.data}), 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                jsend.error("INVALID REQUEST"), 
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            jsend.success({"invoice": serializer.data}),
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            jsend.success({"invoice": "Successfully Deleted"}),
            status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"])
    def update_invoice(self, request, pk=None):
        if self.queryset.filter(id=pk).exists():
            self.queryset.filter(id=pk).update(**request.data)
            inv = self.queryset.get(id=pk)
            serializer = self.serializer_class(inv)
            return Response(
                    jsend.success({"invoice": serializer.data}),
                    status=status.HTTP_200_OK,
                )
        else:
             return Response(
                (jsend.error("Invoice not found")), status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False)
    def get_total_invoice(self, request):
        total_invoice = Invoice.objects.count()
        return Response(
                    jsend.success({"invoice": {"total": total_invoice}}),
                    status=status.HTTP_200_OK,
                )