# django rest
from rest_framework.response import Response
from rest_framework import (
    generics, status, permissions, viewsets
)

# django
from django.contrib.auth import authenticate

# simple_jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# serializers
from .serializers import (
    RegisterVeterinary, VeterinaryInfo
)

# repositories
from veterinaries.domain.jwt_repository import jwtr
from veterinaries.domain.veterinary_repository import vetr

# send email
from send_email.aplication.confirm_email import send_email


class Register(generics.GenericAPIView):
    
    serializer_class = RegisterVeterinary
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email(request, serializer.instance, 'vet')
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
                # access token is added to table outstandingtoken
                jwtr.create_outstandingtoken(
                    instance=veterinary_instance,
                    token=serializer.validated_data['access']
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


class Logout(generics.GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        if not request.data.get('refresh_token'):
            msg = {
                'detail':'Refresh token is required.'
            }
            return Response(
                data=msg,
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json',
            )
        
        # refresh token is added to table BlacklistedToken
        try:
            refresh_token = RefreshToken(token=request.data.get('refresh_token'))
        except TokenError as e:
            msg = {
                'detail':str(e),
            }
            return Response(
                data=msg,
                status=status.HTTP_401_UNAUTHORIZED,
                content_type='application/json',
            )
        refresh_token.blacklist()
        
        # access token is added to table BlacklistedToken
        jwtr.create_blacklistedtoken(
            token=request.headers.get('Authorization').split(' ')[1]
        )
        msg = {
            'detail':'Sesión cerrada.'
        }
        return Response(
            data=msg,
            status=status.HTTP_200_OK,
            content_type='application/json',
        )


class Veternary(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = VeterinaryInfo
    
    def get_queryset(self):
        return vetr.get_all()
    
    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        if page:
            serializer = self.serializer_class(page, many=True, context={'kwargs':kwargs})
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
                content_type='application/json'
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'kwargs':kwargs})
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
            content_type='application/json'
        )