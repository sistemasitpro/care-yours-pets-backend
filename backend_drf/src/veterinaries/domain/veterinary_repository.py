# Django
from django.contrib.auth import get_user_model

# models
from veterinaries.models import Veterinaries


class Repository:
    """
    Encapsulates operations CRUD on the Veterinaries models.
    
    Attributes:
        models (Model): The currently active user model.
    """
    
    def __init__(self) -> None:
        self.model = get_user_model()
    
    def create(self, data:dict) -> Veterinaries:
        return self.model.objects.create_veterinary(
            nif_cif=data['nif_cif'],
            name=data['name'],
            description=data['description'],
            city_id=data['city_id'],
            address=data['address'],
            email=data['email'],
            phone_number=data['phone_number'],
            password=data['password'],
        )

    def get_all(self) -> Veterinaries | None:
        return self.model.objects.filter(is_active=True).all().only('id', 'name', 'description', 'city_id', 'address', 'phone_number')

    def get_by_id(self, id:str) -> Veterinaries | None:
        return self.model.objects.filter(id=id).only('id', 'name', 'description', 'city_id', 'address', 'phone_number', 'is_active').first()
    
    def get_by_only_id(self, id:str) -> Veterinaries | None:
        return self.model.objects.filter(id=id).only('id').first()

vetr = Repository()