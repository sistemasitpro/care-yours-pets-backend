# Django
from django.contrib.auth import get_user_model

# models
from veterinaries.models import Veterinaries


class Repository:
    """
    Encapsulates operations CRUD on the Veterinaries models.
    """
    
    def __init__(self) -> None:
        self.models = get_user_model()
    
    def create(self, data:dict) -> Veterinaries:
        return self.models.objects.create_veterinary(
            nif_cif=data['nif_cif'],
            name=data['name'],
            description=data['description'],
            city_id=data['city_id'],
            address=data['address'],
            email=data['email'],
            phone_number=data['phone_number'],
            password=data['password'],
        )

vetr = Repository()