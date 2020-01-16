from django.contrib.auth.backends import ModelBackend
from .models import User

class NewCustomAuthBackend(ModelBackend):
    """Logs in user with email and password."""

    def authenticate(self, request, email=None, password=None):
        try:
            return User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None
    
    # get a user object
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None