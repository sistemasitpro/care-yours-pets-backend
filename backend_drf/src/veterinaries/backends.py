# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# models
from veterinaries.models import Veterinaries


class NIFCIFBackend(ModelBackend):
    """
    A custom authentication backend that authenticates users based on their NIF/CIF.
    Inherits from Django's ModelBackend.
    """
    
    def authenticate(self, request, nif_cif:str, password:str) -> Veterinaries | None:
        try:
            instance = get_user_model().objects.get(nif_cif=nif_cif)
        except get_user_model().DoesNotExist:
            return None
        if instance.check_password(password):
            return instance
        return None