from .base import *

# database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portland_python_local',
        'USER': 'portland_python',
        'PASSWORD': 'snakes_and_beer',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'

# cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# debug toolbar

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# Django extensions

INSTALLED_APPS += ('django_extensions', )

SHELL_PLUS = "ipython"

# Testing

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
