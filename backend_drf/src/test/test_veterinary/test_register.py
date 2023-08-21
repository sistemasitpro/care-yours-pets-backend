# django rest
from rest_framework.test import  APITestCase
from rest_framework  import status

# django
from django.urls import reverse

# factory
from test.factory.veterinary import vetf

# python
import json

# models
from veterinaries.models import Veterinaries
from models_nestjs.models import Provinces, Cities

#import pdb; pdb.set_trace()


class Test(APITestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        province_instance = Provinces.objects.create(
            name='Provincia 1',
        )
        cls.cities_instance = Cities.objects.create(
            province_id=province_instance,
            name='Localidad 1',
        )
        cls.model = Veterinaries
        cls.url = reverse('register')
    
    def setUp(self) -> None:
        self.JSON = vetf.build_JSON(self.cities_instance.id)
        self.JSON_invalid = vetf.build_JSON_invalid()
    
    def test_register(self) -> None:
        # the status code of the request is checked
        response =self.client.post(self.url, self.JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # verifying the existence of the veterinarian in the database
        veterinary_exists = self.model.objects.filter(email=self.JSON['email']).exists()
        self.assertTrue(veterinary_exists)
        
        # verifying registration data
        veterinary_instance = self.model.objects.filter(email=self.JSON['email']).only('nif_cif', 'name', 'description', 'city_id', 'address', 'email', 'phone_number').first()
        self.assertEqual(veterinary_instance.nif_cif, self.JSON['nif_cif'])
        self.assertEqual(veterinary_instance.name, self.JSON['name'])
        self.assertEqual(veterinary_instance.description, self.JSON['description'])
        self.assertEqual(veterinary_instance.address, self.JSON['address'])
        self.assertEqual(veterinary_instance.email, self.JSON['email'])
        self.assertEqual(veterinary_instance.phone_number, self.JSON['phone_number'])
        
    def test_if_send_empty_JSON(self) -> None:
        # the status code of the request is checked
        JSON = {}
        response =self.client.post(self.url, JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # verifying the existence of the veterinarian in the database
        veterinary_exists = self.model.objects.filter(email=self.JSON['email']).exists()
        self.assertFalse(veterinary_exists)
    
    def test_if_JSON_data_invalid(self) -> None:
        # the status code of the request is checked
        response = self.client.post(self.url, self.JSON_invalid, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # verifying the existence of the veterinarian in the database
        veterinary_exists = self.model.objects.filter(email=self.JSON_invalid['email']).exists()
        self.assertFalse(veterinary_exists)