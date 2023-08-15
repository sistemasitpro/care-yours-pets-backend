# models
from veterinaries.models import Veterinaries

# faker
from faker import Faker

# python
import random


faker = Faker('es-ES')


class VeterinaryFactory:
    
    def __init__(self) -> None:
        self.model = Veterinaries
    
    def build_JSON(self, city_id) -> dict:
        valid_nif_cif = [faker.cif(), faker.nif()]
        return {
            'nif_cif': random.choice(valid_nif_cif),
            'name':f'{faker.first_name()} {faker.last_name()}',
            'description': faker.paragraph(nb_sentences=5),
            'city_id':city_id,
            'address': faker.address(),
            'email': faker.email(),
            'phone_number': faker.phone_number(),
            'password':'Aaa123456789',
        }
    
    def build_JSON_invalid(self) -> dict:
        return {
            'nif_cif':f'{faker.bothify(text="#########")}',
            'name':f'{faker.bothify(text="#########")}',
            'description': faker.paragraph(nb_sentences=5),
            'city_id':1,
            'address': faker.address(),
            'email': 'email@.com',
            'phone_number':f'{faker.bothify(text="###########")}',
            'password':'123456789',
        }

vetf = VeterinaryFactory()