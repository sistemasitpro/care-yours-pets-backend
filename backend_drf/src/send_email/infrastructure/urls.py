# django
from django.urls import path

# views
from .views import (
    SendEmail, confirm_email
)


urlpatterns = [
    path('v1/send-email/confirm', view=SendEmail.as_view(), name='send_email'),
    path('v1/confirm-email/<str:rol>/<str:idb64>/<str:tkn>', view=confirm_email, name='confirm_email'),
]