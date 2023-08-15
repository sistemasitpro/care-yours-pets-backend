from django.contrib import admin
from veterinaries.models import (
    Veterinaries, VeterinaryService, ServiceCategories
)


class VeterinariesAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'nif_cif', 'name', 'city_id', 'address', 'email', 'phone_number', 'is_active', 'date_joined', 'last_login')
    #search_fields = ('id', 'nif_cif', 'name', 'city_id')


class VeterinaryServiceAdminPanel(admin.ModelAdmin):
    list_display = ('uid', 'veterinary_id', 'service_category', 'service_name', 'price')
    #search_fields = ('uid', 'service_name', 'veterinary_id', 'service_category')


class ServiceCategoriesAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    #search_fields = ('name', 'id')


admin.site.register(Veterinaries, VeterinariesAdminPanel)
admin.site.register(VeterinaryService, VeterinaryServiceAdminPanel)
admin.site.register(ServiceCategories, ServiceCategoriesAdminPanel)
