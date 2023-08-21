"""
WSGI config for settings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import config


if config('ENVIRONMENT_STATUS') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_settings.settings.local')
if config('ENVIRONMENT_STATUS') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_settings.settings.production')

application = get_wsgi_application()
