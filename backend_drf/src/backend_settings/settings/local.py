from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1","localhost","pre.api.lcareyourspets.duckdns.org"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE_LOCAL'),
        'NAME': config('NAME_LOCAL'),
        'USER': config('USER_LOCAL'),
        'PASSWORD': config('PASSWORD_LOCAL'),
        'HOST': config('HOST_LOCAL'),
        'PORT': config('PORT_LOCAL'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'