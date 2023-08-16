from django.db import models


class Cities(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    province_id = models.ForeignKey(
        db_column='province_id',
        to='Provinces',
        to_field='id',
        on_delete=models.DO_NOTHING,
        null=False,
    )
    name = models.CharField(max_length=100, null=False)
    
    class Meta:
        db_table='cities'
        verbose_name = "city"
        verbose_name_plural = "cities"


class Provinces(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=100, null=False)
    
    class Meta:
        db_table='provinces'
        verbose_name = "province"
        verbose_name_plural = "provinces"


class Users(models.Model):
    id = models.UUIDField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=200, null=False)
    email = models.EmailField(
        db_column='email',
        max_length=100,
        unique=True,
        null=False,
    )
    phone_number = models.CharField(
        db_column='phone_number',
        max_length=16,
        unique=True,
        null=False,
    )
    city_id = models.ForeignKey(
        db_column='city_id',
        to='Cities',
        to_field='id',
        on_delete=models.DO_NOTHING,
    )
    address = models.CharField(db_column='address', max_length=300, null=False)
    password = models.CharField(db_column='password', max_length=128, null=False)
    is_active = models.BooleanField(db_column='is_active', default=False, null=False)
    is_superuser = models.BooleanField(db_column='is_superuser', null=False)
    at_created = models.DateTimeField(db_column='at_created', null=False)
    last_login = models.DateTimeField(db_column='last_login',null=True)
    
    class Meta:
        db_table='users'
        verbose_name = "user"
        verbose_name_plural = "users"
    
    def __str__(self):
        return self.name
