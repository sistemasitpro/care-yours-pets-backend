# models
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken, BlacklistedToken
)


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
    
    def create_outstandingtoken(self, data:dict) -> OutstandingToken:
        """
        Creates a new instance of the OutstandingToken model with the provided data.

        Parameters:
            data (dict): A dictionary containing the data to create a new OutstandingToken instance.

        Returns:
            OutstandingToken: The new OutstandingToken instance that has been created.
        """
        
        return self.model_outstandingtoken.objects.create(
            user=data['veterinary_instance'],
            jti=data['jti'],
            token=data['token'],
            created_at=data['created_at'],
            expires_at=data['expires_at'],
        )

    def create_blacklistedtoken(self, access_token:OutstandingToken) -> BlacklistedToken:
        """
        Creates a new instance of the BlacklistedToken model with the provided OutstandingToken instance.

        Parameters:
            access_token (OutstandingToken): An instance of OutstandingToken to be blacklisted.

        Returns:
            BlacklistedToken: The new BlacklistedToken instance that has been created.
        """
        
        return self.model_blacklistedtoken.objects.create(
            token=access_token,
        )
    
    def get_by_only_jti(self, jti:str) -> OutstandingToken | None:
        """
        Gets an instance of the OutstandingToken model by its jti attribute.

        Parameters:
            jti (str): The jti of the OutstandingToken instance to retrieve.

        Returns:
            OutstandingToken | None: The OutstandingToken instance with the provided jti, or None if there is none.
        """
        
        return self.model_outstandingtoken.objects.filter(jti=jti).only('id').first()

jwtr = Repository()