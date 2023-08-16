# django rest
from rest_framework.test import  APITestCase, APIClient
from rest_framework  import status

# django
from django.urls import reverse

# factory
from test.factory.veterinary import vetf

# models
from models_nestjs.models import Provinces, Cities

#import pdb; pdb.set_trace()


class Test(APITestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        province_instance = Provinces.objects.create(
            name='Provincia 3',
        )
        cls.cities_instance = Cities.objects.create(
            province_id=province_instance,
            name='Localidad 3',
        )
    
    def setUp(self) -> None:
        # instance
        factory = vetf.create_instance(self.cities_instance)
        self.veterinary_instance = factory['instance']
        self.veterinary_instance.is_active = True
        self.veterinary_instance.save()
        
        # login request data
        data = factory['data']
        JSON = {
            'nif_cif':data['nif_cif'],
            'password':data['password'],
        }
        response = self.client.post(reverse('login'), JSON, format='json')
        
        # obtain access_token and refresh_token
        self.JSON = {
            'refresh_token':response.data['refresh_token'],
        }
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access_token"]}')
        
        # path
        kwargs = {
            'id':str(self.veterinary_instance.id),
        }
        self.url = reverse('logout', kwargs=kwargs)
    
    def test_logout(self) -> None:
        # the status code of the request is checked
        response = self.client.post(self.url, self.JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)