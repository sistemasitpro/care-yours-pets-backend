# django rest
from rest_framework.test import  APITestCase
from rest_framework  import status

# django
from django.urls import reverse

# factory
from test.factory.veterinary import vetf

# models
from models_nestjs.models import Provinces, Cities


class Test(APITestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        province_instance = Provinces.objects.create(
            name='Provincia 2',
        )
        cls.cities_instance = Cities.objects.create(
            province_id=province_instance,
            name='Localidad 2',
        )
        cls.url = reverse('login')
    
    def setUp(self) -> None:
        # instances
        factory = vetf.create_instance(self.cities_instance)
        veterinary_instance = factory['instance']
        veterinary_instance.is_active = True
        veterinary_instance.save()
        
        # data
        data = factory['data']
        self.JSON = {
            'nif_cif':data['nif_cif'],
            'password':data['password'],
        }
    
    def test_login(self) -> None:
        # the status code of the request is checked
        response = self.client.post(self.url, self.JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)