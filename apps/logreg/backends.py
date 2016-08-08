from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from django.core.exceptions import ValidationError

class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
            #else:
                #raise ValidationError("Some bobooo message")
        except CustomUser.DoesNotExist:
            #raise ValidationError("Some custom message")
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
