from datetime import timedelta
import datetime
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, views
from .models import User, Client

# auth_backend
from .auth_backend import CustomAuthBackend
authenticate = CustomAuthBackend.authenticate

from .serializers import (RegistrationSerializer, 
    ClientSerializer, LoginSerializer)

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
        

