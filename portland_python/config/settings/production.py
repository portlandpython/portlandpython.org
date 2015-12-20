import json
from unipath import Path

from django.core.exceptions import ImproperlyConfigured

from .base import *

BASE_DIR = Path(__file__).ancestor(3)

secrets_path = BASE_DIR.child('config').child('settings', 'secrets.json')

with open(secrets_path) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

DEBUG = False

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Los_Angeles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': 'gardenharmony',
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

SERVER_EMAIL = ''

DEFAULT_FROM_EMAIL = ''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

EMAIL_HOST = ''

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")

EMAIL_PORT = 587

COMPRESS_OFFLINE = True
