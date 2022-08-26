import django_heroku
django_heroku.settings(locals())
from .settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd609hb7fhnb51m',
        'USER': 'uonseawcrjaglk',
        'PASSWORD': '12d1debee3bccbf20bde8e19bcda14cacbdb523f09916f944b5b4ce4b15c9842',
        'HOST': 'ec2-107-22-122-106.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
