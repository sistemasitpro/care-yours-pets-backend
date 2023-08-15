# django
from django.urls import path

# views
from .views import (
    Register
)


urlpatterns = [
    path('v1/veterinary', view=Register.as_view(), name='register'),
]