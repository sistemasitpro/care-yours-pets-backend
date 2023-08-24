# Django
from django.contrib.auth.models import (
    UserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models

# Python
import uuid


class VeterinaryManager(UserManager):
    def _create_veterinary(self, nif_cif:str, name:str, description:str, email:str, city_id, address:str, phone_number:str, password:str, **extra_fields):
        """
        Create and save a veterinary in the database with user information (nif_cif, name, description, email, , city_id, address, phone number and password).
        
        Returns:
            veterinary: Instance of the veterinaries model.
        """
        
        fields = {
            'nif_cif':nif_cif,
            'name':name,
            'description':description,
            'email':email,
            'city_id':city_id,
            'address':address,
            'phone number':phone_number,
            'password':password
        }
        for key, value in fields.items():
            if not value:
                raise ValueError(f"The given {key} must be set")
        veterinary = self.model(
            nif_cif=nif_cif,
            name=name,
            description=description,
            email=self.normalize_email(email),
            city_id=city_id,
            address=address,
            phone_number=phone_number,
            **extra_fields
        )
        veterinary.set_password(password)
        veterinary.save(using=self._db)
        return veterinary
    
    def create_veterinary(self, nif_cif:str, name:str, description:str, email:str,
                          city_id, address:str, phone_number:str, password:str, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_veterinary(nif_cif, name, description, email, city_id,
                                       address, phone_number, password,**extra_fields)
    
    def create_superuser(self, nif_cif:str, name:str, description:str, email:str,
                         city_id, address:str, phone_number:str, password:str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_veterinary(nif_cif, name, description, email, city_id,
                                       address, phone_number, password, **extra_fields)


class Veterinaries(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(db_column='id', default=uuid.uuid4, primary_key=True)
    nif_cif = models.CharField(
        db_column='nif_cif',
        max_length=10,
        unique=True,
        null=False,
        blank=False,
    )
    name = models.CharField(
        db_column='name',
        max_length=200,
        unique=True,
        null=False,
        blank=False,
    )
    description = models.TextField(db_column='description', null=False, blank=False)
    city_id = models.ForeignKey(
        db_column='city_id',
        to='models_nestjs.Cities',
        to_field='id',
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    address = models.CharField(
        db_column='address',
        max_length=300,
        unique=True,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        db_column='email',
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(
        db_column='phone_number',
        max_length=16,
        unique=True,
        null=False,
        blank=False,
    )
    password = models.CharField(
        db_column='password', 
        max_length=128,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(db_column='is_staff', default=False, serialize=False)
    is_superuser = models.BooleanField(db_column="is_superuser", default=False,  serialize=False)
    is_active = models.BooleanField(db_column='is_active', default=False)
    date_joined = models.DateTimeField(db_column='date_joined', auto_now_add=True,  serialize=False)
    last_login = models.DateTimeField(db_column='last_login', null=True, blank=True,  serialize=False)
    
    objects = VeterinaryManager()
    
    USERNAME_FIELD = 'nif_cif'
    REQUIRED_FIELDS = ['name', 'email']
    
    class Meta:
        db_table='veterinaries'
        verbose_name = "veterinary"
        verbose_name_plural = "veterinaries"
    
    def __str__(self):
        return self.name
    

class VeterinaryService(models.Model):
    uid = models.UUIDField(db_column='uid', primary_key=True, default=uuid.uuid4)
    veterinary_id = models.ForeignKey(
        db_column='veterinary_id',
        to='Veterinaries',
        to_field='id',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    service_id = models.ForeignKey(
        db_column='service_id',
        to='Service',
        to_field='id',
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    name = models.CharField(
        db_column='name',
        max_length=200,
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        db_column='price',
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
    )
    
    class Meta:
        db_table='veterinary_service'
        verbose_name = "veterinary_service"
        verbose_name_plural = "veterinary_services"
    
    def __str__(self):
        return self.name


class ServiceCategories(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=100, null=False, unique=True)
    description = models.CharField(db_column='description', max_length=500, null=False)
    
    class Meta:
        db_table='service_categories'
        verbose_name = "service_category"
        verbose_name_plural = "service_categories"
    
    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    category_id = models.ForeignKey(
        db_column='categoty_id',
        to='ServiceCategories',
        to_field='id',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )
    name = models.CharField(db_column='name', null=False, blank=False)
    
    class Meta:
        db_table='service'
        verbose_name = "service"
        verbose_name_plural = "services"
    
    def __str__(self):
        return self.name