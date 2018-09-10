from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if not DEBUG:
    ALLOWED_HOSTS = ['150.246.47.235']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airport_review',
        'USER': 'root',
        'PASSWORD': '9h2~*j-Q6pBA',
        'HOST': '',
        'PORT': '',
    }
}