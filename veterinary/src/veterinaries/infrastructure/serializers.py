# dejango rest
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

# dejango rest
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

# django
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import (
    RegexValidator, MaxLengthValidator, MinLengthValidator
)

# repositories
from veterinaries.domain.veterinary_repository import vetr


class CustomErrorMessages(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customized error messages
        msg = {
            'required': 'Este campo es requerido.',
            'blank': 'Este campo no puede estar en blanco.',
            'null':'Este campo no puede ser nulo.',
        }
        self.fields['nif_cif'].error_messages.update(msg)
        self.fields['name'].error_messages.update(msg)
        self.fields['description'].error_messages.update(msg)
        self.fields['city_id'].error_messages.update(msg)
        self.fields['address'].error_messages.update(msg)
        self.fields['email'].error_messages.update(msg)
        self.fields['phone_number'].error_messages.update(msg)


class RegisterVeterinary(CustomErrorMessages):
    
    model = get_user_model()
    
    nif_cif = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=model.objects.values('nif_cif'),
                message="Este NIF/CIF ya está en uso."
            ),
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])[A-Za-z0-9][0-9]{7}[A-Za-z0-9]$',
                message='NIF/CIF inválido.',
                code='invalid_data',
            ),
            MaxLengthValidator(
                limit_value=10,
                message='El valor ingresado supera el número máximo de caracteres permitidos (10).',
            )
        ]
    )
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=model.objects.values('name'),
                message="Este nombre ya está en uso."
            ),
            RegexValidator(
                regex=r'^(?=.*[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ])[a-zA-Z0-9áéíóúüñÁÉÍÓÚÜÑ.,\-() ]+$',
                message='Nombre inválido.',
                code='invalid_data',
            ),
            MaxLengthValidator(
                limit_value=200,
                message='El valor ingresado supera el número máximo de caracteres permitidos (200).',
            )
        ]
    )
    address = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=model.objects.values('address'),
                message="Esta dirección ya está en uso."
            ),
            MaxLengthValidator(
                limit_value=300,
                message='El valor ingresado supera el número máximo de caracteres permitidos (300).',
            )
        ]
    )
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=model.objects.values('email'),
                message="Este correo electrónico ya está en uso."
            ),
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                message='Correo electrónico inválido.',
                code='invalid_data',
            ),
            MaxLengthValidator(
                limit_value=100,
                message='El valor ingresado supera el número máximo de caracteres permitidos (100).',
            )
        ]
    )
    phone_number = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=model.objects.values('phone_number'),
                message="Este número de teléfono ya está en uso."
            ),
            RegexValidator(
                regex=r'^\+?[0-9]{1,3}[ -]?\(?[0-9]{1,3}\)?[ -]?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,9}$',
                message='Número de teléfono inválido.',
                code='invalid_data',
            ),
            MaxLengthValidator(
                limit_value=16,
                message='El valor ingresado supera el número máximo de caracteres permitidos (16).',
            )
        ]
    )
    password = serializers.CharField(
        write_only=True,
        style={
            'input_type':'password',
        },
        validators=[
            MinLengthValidator(
                limit_value=8,
                message='La contraseña debe ser de almenos 8 caracteres.'
            )
        ]
    )
    
    class Meta:
        model = get_user_model()
        fields = ['nif_cif', 'name', 'description', 'city_id', 'address', 'email', 'phone_number', 'password']
    
    # Validations
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(
                detail=str(e),
                code='Invalid_data',
            )
        return value
    
    # methods
    def create(self, validated_data):
        return vetr.create(data=validated_data)