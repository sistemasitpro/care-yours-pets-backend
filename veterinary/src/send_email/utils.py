# Django
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone

# Six
import six

# Python
from datetime import timedelta

# repositories
from send_email.repository import tkdr


class GenerateToken(PasswordResetTokenGenerator):
    
    def _make_hash_value(self, instance, timestamp:int) -> str:
        return six.text_type(instance.id)+six.text_type(timestamp)+six.text_type(instance.is_active)
    
    def validate_expiration(self, token:str) -> bool:
        datetime_created = tkdr.get_datetime_created(token)
        time_limit = datetime_created + timedelta(minutes=10)
        current_datetime = timezone.now()
        if current_datetime < time_limit:
            return True
        return False

token = GenerateToken()