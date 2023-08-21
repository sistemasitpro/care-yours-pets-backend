# django rest
from rest_framework import status

# simple_jwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# repositories
from veterinaries.domain.jwt_repository import jwtr


class VeterinaryLogout:
    
    error = {}
    status =  None
    
    def __init__(self, request, data) -> None:
        self.request = request
        self.data = data
    
    def logout_veterinary(self):
        if not self.data.get('refresh_token'):
            self.status = status.HTTP_400_BAD_REQUEST
            return self.error.update({
                'detail':'Refresh token is required.'
            })
        
        # refresh token is added to table BlacklistedToken
        try:
            refresh_token = RefreshToken(token=self.data.get('refresh_token'))
        except TokenError as e:
            self.status = status.HTTP_401_UNAUTHORIZED
            return self.error.update(str(e))
        refresh_token.blacklist()
        
        # access token is added to table BlacklistedToken
        jwtr.create_blacklistedtoken(
            token=self.request.headers.get('Authorization').split(' ')[1]
        )
        self.status = status.HTTP_200_OK
        return self.error.update({
            'detail':'Sesión cerrada.'
        })
        
    def is_complete(self) -> bool:
        self.logout_veterinary()
        if self.status is status.HTTP_200_OK:
            return True
        return False