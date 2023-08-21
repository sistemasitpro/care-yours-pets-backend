# django rest
from rest_framework.test import  APITestCase, APIClient
from rest_framework  import status

# django
from django.urls import reverse

# simple jwt
from rest_framework_simplejwt.tokens import RefreshToken

# factory
from test.factory.veterinary import vetf

# models
from veterinaries.domain.jwt_repository import jwtr
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
        
        # obtain access_token and refresh_token
        self.refresh_token = RefreshToken.for_user(self.veterinary_instance)
        self.access_token = str(self.refresh_token.access_token)
        self.JSON = {
            'refresh_token':str(self.refresh_token),
        }
        jwtr.create_outstandingtoken(
            instance=self.veterinary_instance,
            token=self.access_token,
        )
        
        # authentication
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        # path
        kwargs = {
            'id':self.veterinary_instance.id,
        }
        self.url = reverse('logout', kwargs=kwargs)
    
    def test_logout(self) -> None:
        # the status code of the request is checked
        response = self.client.post(self.url, self.JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)