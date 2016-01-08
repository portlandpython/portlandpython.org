from os import environ
import json
from unipath import Path
import dj_database_url

from django.core.exceptions import ImproperlyConfigured

from .base import *

BASE_DIR = Path(__file__).ancestor(3)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Los_Angeles'

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = environ.get('SECRET_KEY')

COMPRESS_OFFLINE = True
