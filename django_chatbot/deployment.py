import os
from .settings import *
from .settings import BASE_DIR

OPENAI_KEY = os.environ['OPENAI_KEY']

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]

DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


DATABASES = {'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('Azure_SQL_NAME'),
        'HOST': os.environ.get('Azure_SQL_HOST'),
        'USER': os.environ.get('Azure_SQL_USER'),
        'PORT':os.environ.get('Azure_SQL_PORT'),
        'PASSWORD': os.environ.get('Azure_SQL_PASSWORD'),
        'OPTIONS': {'driver': 'ODBC Driver 18 for SQL Server',},
        }
    }
    # set this to False if the backend does not support using time zones
USE_TZ = False