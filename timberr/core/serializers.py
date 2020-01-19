from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from .models import User, Client, Invoice

from django.db.models import Q


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "company_name",
            "office_address",
            "office_telephone"

        )
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id",)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=make_password(validated_data["password"]),
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            company_name=validated_data["company_name"],
            office_address=validated_data["office_address"],
            office_telephone=validated_data["office_telephone"],
        )
        user.save()
        return user
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        style={"input_type": "email"}, source="user.email"
        )
    password = serializers.CharField(
        style={"input_type": "password"}, source="user.password"
    )

    class Meta:
        model = User
        fields = ["email", "username", "password"]
        

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "full_name",
            "company_name",
            "telephone",
            "about",
            "address",
            "city",
            "state",
            "country",
            "zipcode",
            "created_by",
        )

        read_only_fields = ("id", )

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class InvoiceSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Invoice
        fields = (
            "id",
            "invoice_id",
            "due_date",
            "payment_term",
            "shipping_address",
            "vat",
            "dispatch_personnel",
            "client",
            "created_by",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)
