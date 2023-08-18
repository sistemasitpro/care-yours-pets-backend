from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1","localhost","pre.api.careyourspets.duckdns.org"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE_PRODUCTION'),
        'NAME': config('NAME_LOCAL_PRODUCTION'),
        'USER': config('USER_LOCAL_PRODUCTION'),
        'PASSWORD': config('PASSWORD_LOCAL_PRODUCTION'),
        'HOST': config('HOST_LOCAL_PRODUCTION'),
        'PORT': config('PORT_LOCAL_PRODUCTION'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'