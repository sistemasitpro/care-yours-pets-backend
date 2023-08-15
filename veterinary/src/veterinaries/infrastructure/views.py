# django rest
from rest_framework.response import Response
from rest_framework import (
    generics, status
)

# django
from django.contrib.auth import authenticate

# simple_jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# python
from datetime import datetime
import jwt

# settings
from settings.settings import SIMPLE_JWT

# serializers
from .serializers import (
    RegisterVeterinary
)

# repositories
from veterinaries.domain.jwt_repository import jwtr


class Register(generics.GenericAPIView):
    
    serializer_class = RegisterVeterinary
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = {
                'detail':f'Resgistro completado. Se ha enviado un enlace de activación de cuenta al correo {serializer.validated_data["email"]}'
            }
            return Response(
                data=msg,
                status=status.HTTP_201_CREATED,
                content_type='application/json'
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            content_type='application/json'
        )


class Login(TokenObtainPairView):
    
    serializer_class = TokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        veterinary_instance = authenticate(
            request,
            nif_cif=request.data.get('nif_cif'),
            password=request.data.get('password')
        )
        if not veterinary_instance:
            msg = {
                'detail':'Credenciales inválidas.'
            }
            return Response(
                data=msg,
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json',
            )
        if veterinary_instance.is_active:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                # access is added to table outstandingtoken
                decoded_access_token = jwt.decode(
                    jwt=serializer.validated_data['access'],
                    key=SIMPLE_JWT['SIGNING_KEY'],
                    algorithms=[SIMPLE_JWT['ALGORITHM']],
                )
                jwtr.create_outstandingtoken(
                    data={
                        'veterinary_instance':veterinary_instance,
                        'jti':decoded_access_token['jti'],
                        'token':serializer.validated_data['access'],
                        'created_at':datetime.now(),
                        'expires_at':datetime.fromtimestamp(decoded_access_token['exp']).isoformat(),
                    }
                )
                msg = {
                    'access_token':serializer.validated_data['access'],
                    'refresh_token':serializer.validated_data['refresh'],
                }
                return Response(
                    data=msg,
                    status=status.HTTP_200_OK,
                    content_type='application/json',
                )
        msg = {
            'detail':'Su cuenta aun no esta activa.'
        }
        return Response(
            data=msg,
            status=status.HTTP_401_UNAUTHORIZED,
            content_type='application/json',
        )