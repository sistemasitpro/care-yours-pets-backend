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
    
    def user_can_authenticate(self, veterinary:Veterinaries) -> bool:
        if veterinary.is_active:
            return True
        return False
    
    def authenticate(self, request, nif_cif:str, password:str) -> Veterinaries | None:
        if nif_cif is None or password is None:
            return None
        try:
            veterinary = get_user_model().objects.get(nif_cif=nif_cif)
        except get_user_model().DoesNotExist:
            return None
        if veterinary.check_password(password) and self.user_can_authenticate(veterinary):
            return veterinary
        return None