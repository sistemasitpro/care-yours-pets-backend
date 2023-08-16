# django
from django.urls import path

# simpleJWT
from rest_framework_simplejwt.views import TokenRefreshView

# views
from .views import (
    Register, Login, Logout
)


urlpatterns = [
    path('v1/veterinary', view=Register.as_view(), name='register'),
    
    # authentication
    path('v1/auth/login', view=Login.as_view(), name='login'),
    path('v1/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/auth/logout/<str:id>', view=Logout.as_view(), name='logout'),
]