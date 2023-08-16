# django rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import (
    generics, status, permissions
)

# django
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.shortcuts import render

# repositories
from veterinaries.domain.veterinary_repository import vetr
from models_nestjs.repository import usr

# project
from send_email.aplication.confirm_email import send_email
from send_email.utils import token


class SendEmail(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        rol = request.data.get('rol')
        if id and rol:
            instance = usr.get_by_id(id=id)
            send_email(request, instance, rol)
            return Response(
                status=status.HTTP_200_OK,
            )
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def confirm_email(request, rol, idb64, tkn):
    id = str(force_str(urlsafe_base64_decode(idb64)))
    if rol == 'user':
        instance = usr.get_by_id(id=id)
        if not instance:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        check_token = token.check_token(instance, tkn)
        check_expiration = token.validate_expiration(tkn)
        if instance and check_token and check_expiration:
            instance.is_active = True
            instance.save()
            return render(
                request,
                template_name='confirm_ok.html',
                status=status.HTTP_200_OK
            )
        return render(
            request,
            template_name='confirm_error.html',
            status=status.HTTP_401_UNAUTHORIZED
        )
    if rol == 'vet':
        instance = vetr.get_by_id(id=id)
        if not instance:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        check_token = token.check_token(instance, tkn)
        check_expiration = token.validate_expiration(tkn)
        if instance and check_token and check_expiration:
            instance.is_active = True
            instance.save()
            return render(
                request,
                template_name='confirm_ok.html',
                status=status.HTTP_200_OK
            )
        return render(
            request,
            template_name='confirm_error.html',
            status=status.HTTP_401_UNAUTHORIZED
        )