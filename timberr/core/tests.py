from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
# Create your tests here.


class APITest(APITestCase):
    list_create_client_url = reverse('list-create-client')

    def setUp(self):
        # ensure a new user can send a post request
        data = {
            "username": "adams2",
            "email": "adams2@gmail.com",
            "first_name": "Adams",
            "last_name": "James",
            "password": "somepassword",
            "company_name": "Bloverse",
            "office_address": "123, Stan Road",
            "office_telephone": 234816333641
            }
        signup_url = reverse('register')
        self.user = self.client.post(signup_url, data, format='json')

        # obtain a JWT Token
        login_url = reverse('login')
        response = self.client.post(login_url, data={'email': 'adams2@gmail.com', 'password': 'somepassword'})
        res = eval(response.content.decode("utf-8"))
        self.token=res['data']['token']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token)

    def test_list_clients_authenticated(self):
        response = self.client.get(self.list_create_client_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_clients_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_create_client_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_client(self):
        data = {
            "full_name": "James Tancredi-B",
            "company_name": "Dev Inc",
            "phone_number": 455123456789,
            "about": "He is a guy",
            "address": "A fucking unknown place",
            "city": "London",
            "state": "London",
            "country": "England",
            "zipcode": "877",
            "created_by": 1
        }
        response = self.client.post(self.list_create_client_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
