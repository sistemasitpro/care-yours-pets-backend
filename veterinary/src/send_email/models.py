# django
from django.utils import timezone
from django.db import models


class TokenDjango(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    token = models.CharField(
        db_column='token',
        max_length=255,
        unique=True,
        null=False,
    )
    at_created = models.DateTimeField(db_column='at_created', null=False)
    
    class Meta:
        db_table='token_django'
        verbose_name = "token_django"
        verbose_name_plural = "tokens_django"
    
    def __str__(self):
        return self.token
