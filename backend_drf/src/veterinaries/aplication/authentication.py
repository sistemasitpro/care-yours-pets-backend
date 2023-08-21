# django_rest
from rest_framework import status

# Django
from django.contrib.auth import authenticate

# models
from veterinaries.models import Veterinaries


class VeterinaryAuth:
    
    error = {}
    status = None
    instance = None
    
    def __init__(self, request, data) -> None:
        self.request = request
        self.data = data
    
    def authenticate_veterinary(self) -> dict | Veterinaries:
        nif_cif = self.data.get('nif_cif')
        password = self.data.get('password')
        if not nif_cif and not password:
            self.status = status.HTTP_400_BAD_REQUEST
            return self.error.update({
                'detail':'Las credenciales son requeridas.'
            })
        veterinary_instance = authenticate(
            request=self.request,
            nif_cif=nif_cif,
            password=password
        )
        if not veterinary_instance:
            self.status = status.HTTP_401_UNAUTHORIZED
            return self.error.update({
                'detail':'Credenciales inválidas.'
            })
        if not veterinary_instance.is_active:
            self.status = status.HTTP_401_UNAUTHORIZED
            return self.error.update({
                'detail':'No has activado tu cuenta.'
            })
        self.status = status.HTTP_200_OK
        self.instance = veterinary_instance

    def is_complete(self) -> bool:
        self.authenticate_veterinary()
        if self.status is status.HTTP_200_OK:
            return True
        return False