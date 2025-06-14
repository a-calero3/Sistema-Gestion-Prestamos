from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Cookies seguras (para desarrollo, deben ser False)
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False