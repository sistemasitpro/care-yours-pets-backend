# django
from django.utils.timezone import make_aware

# simple jwt
from rest_framework_simplejwt.utils import datetime_from_epoch

# models
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken, BlacklistedToken
)
from veterinaries.models import Veterinaries

# settings
from settings_backend.settings.base import SIMPLE_JWT

# python
from datetime import datetime
import jwt


class Repository:
    """
    Encapsulates operations CRUD on the OutstandingToken and BlacklistedToken models.
    
    Attributes:
        model_outstandingtoken (Model): The OutstandingToken model.
        model_blacklistedtoken (Model): The BlacklistedToken model.
    """
    
    def __init__(self) -> None:
        self.model_outstandingtoken = OutstandingToken
        self.model_blacklistedtoken = BlacklistedToken
    
    def decoded_token(self, token:str) -> dict:
        return jwt.decode(
            jwt=token,
            key=SIMPLE_JWT['SIGNING_KEY'],
            algorithms=[SIMPLE_JWT['ALGORITHM']],
        )
    
    def create_outstandingtoken(self, instance:Veterinaries, token:str) -> OutstandingToken:
        data = self.decoded_token(token)
        return self.model_outstandingtoken.objects.create(
            user=instance,
            jti=data['jti'],
            token=token,
            created_at=make_aware(datetime.now()),
            expires_at=datetime_from_epoch(data['exp']),
        )

    def create_blacklistedtoken(self, token:str) -> BlacklistedToken:
        data = self.decoded_token(token)
        return self.model_blacklistedtoken.objects.create(
            token=self.get_by_only_jti(data['jti']),
        )
    
    def get_by_only_jti(self, jti:str) -> OutstandingToken | None:
        return self.model_outstandingtoken.objects.filter(jti=jti).only('id').first()

jwtr = Repository()