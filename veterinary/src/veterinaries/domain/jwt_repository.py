# models
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken, BlacklistedToken
)


class Repository:
    """
    Encapsulates operations CRUD on the OutstandingToken and BlacklistedToken models.
    """
    
    def __init__(self) -> None:
        self.model_outstandingtoken = OutstandingToken
        self.model_blacklistedtoken = BlacklistedToken
    
    def create_outstandingtoken(self, data:dict) -> OutstandingToken:
        return self.model_outstandingtoken.objects.create(
            user=data['veterinary_instance'],
            jti=data['jti'],
            token=data['token'],
            created_at=data['created_at'],
            expires_at=data['expires_at'],
        )

    def create_blacklistedtoken(self, access_token:OutstandingToken) -> BlacklistedToken:
        return self.model_blacklistedtoken.objects.create(
            token=access_token,
        )
    
    def get_by_only_jti(self, jti:str) -> OutstandingToken | None:
        return self.model_outstandingtoken.objects.filter(jti=jti).only('id').first()

jwtr = Repository()