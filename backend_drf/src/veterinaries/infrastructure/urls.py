# django
from django.urls import path, include

# simpleJWT
from rest_framework_simplejwt.views import TokenRefreshView

# views
from .views import (
    Register, Login, Logout, CreateService
)


urlpatterns = [
    path('v1/veterinary', view=Register.as_view(), name='register'),
    path('v1/auth/signin', view=Login.as_view(), name='login'),
    path('v1/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/auth/logout/<str:id>', view=Logout.as_view(), name='logout'),
    path('v1/', include('veterinaries.infrastructure.routers')),
    path('v1/veterinary/service', view=CreateService.as_view(), name='create_service'),
]