from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200, blank=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=250, unique=True)
    company_name = models.CharField(max_length=200, blank=False)
    office_address = models.CharField(max_length=200, blank=False)
    office_telephone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ("-date_joined",)


class Client(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    company_name = models.CharField(max_length=200, blank=False)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    zipcode = models.CharField(max_length=200, blank=False)
    date_created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-date_created",)


class Invoice(models.Model):
    PAYMENT_TERM = (
            ("End of Month", "End of Month"), 
            ("End of Quater", "End of Quater"),
            ("End of Year", "End of Year"),
        )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=10, blank=False, unique=True)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice', null=True)
    payment_term = models.CharField(max_length=200, choices=PAYMENT_TERM, default="End of Month")
    shipping_address = models.TextField(blank=False)
    vat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    dispatch_personnel = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.invoice_id

    class Meta:
        ordering = ("-date_created",)



