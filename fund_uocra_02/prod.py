from .settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dcgktfooaos327',
        'USER': 'jabhejfdqofqal',
        'PASSWORD': '9b1e48681227e2bdbe42fa85173c99cc04c55d30e60606b6f536e043c9787aac',
        'HOST': 'ec2-54-159-175-38.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import django_heroku
django_heroku.settings(locals())