from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airport_review',
        'USER': 'root',
        # 'PASSWORD': '(Rsk7SvJyf)T',
        'PASSWORD': '65t00Uof',
        'HOST': '',
        'PORT': '',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]