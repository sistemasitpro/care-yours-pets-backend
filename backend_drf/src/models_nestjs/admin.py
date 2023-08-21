from django.contrib import admin
from models_nestjs.models import (
    Cities, Provinces,
)


class CitiesAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'province_id', 'name')
    #search_fields = ('name', 'id', 'province_id')


class ProvincesAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'name')
    #search_fields = ('name', 'id')


admin.site.register(Cities, CitiesAdminPanel)
admin.site.register(Provinces, ProvincesAdminPanel)