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
