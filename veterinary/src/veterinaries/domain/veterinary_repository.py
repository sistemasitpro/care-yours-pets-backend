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
        self.models = get_user_model()
    
    def create(self, data:dict) -> Veterinaries:
        """
        Creates a new instance of the Veterinaries model with the provided data.

        Parameters:
            data (dict): A dictionary containing the data to create a new Veterinaries instance.

        Returns:
            Veterinaries: The new Veterinaries instance that has been created.
        """
        
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

    def get_all(self) -> Veterinaries | None:
        """
        Gets all active instances of the Veterinaries model.

        Returns:
            Veterinaries | None: A list of all active Veterinaries instances, or None if there are none.
        """
        
        return self.models.objects.filter(is_active=True).all().only('id', 'name', 'description', 'city_id', 'address', 'phone_number')

vetr = Repository()