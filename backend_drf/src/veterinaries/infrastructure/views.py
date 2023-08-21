# django rest
from rest_framework.response import Response
from rest_framework import (
    generics, status, permissions, viewsets
)

# simple_jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers
from .serializers import (
    RegisterVeterinary, VeterinaryInfo
)

# repositories
from veterinaries.domain.jwt_repository import jwtr
from veterinaries.domain.veterinary_repository import vetr

# send email
from send_email.aplication.confirm_email import send_email

# aplication
from veterinaries.aplication.authentication import VeterinaryAuth
from veterinaries.aplication.logout import VeterinaryLogout


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
    auth_class = VeterinaryAuth
    
    def post(self, request, *args, **kwargs):
        authentication = self.auth_class(request, data=request.data)
        if not authentication.is_complete():
            return Response(
                data=authentication.error,
                status=authentication.status,
                content_type='application/json'
            )
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # access token is added to table outstandingtoken
            jwtr.create_outstandingtoken(
                instance=authentication.instance,
                token=serializer.validated_data['access']
            )
            msg = {
                'access_token':serializer.validated_data['access'],
                'refresh_token':serializer.validated_data['refresh'],
            }
            return Response(
                data=msg,
                status=authentication.status,
                content_type='application/json',
            )


class Logout(generics.GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    logout_calss = VeterinaryLogout
    
    def post(self, request, *args, **kwargs):
        logout =self.logout_calss(request, data=request.data)
        if not logout.is_complete():
            return Response(
                data=logout.error,
                status=logout.status,
                content_type='application/json'
            )
        return Response(
            data=logout.error,
            status=logout.status,
            content_type='application/json'
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