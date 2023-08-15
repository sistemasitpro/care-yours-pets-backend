# django rest
from rest_framework.response import Response
from rest_framework import (
    generics, status
)

# serializers
from .serializers import (
    RegisterVeterinary
)


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