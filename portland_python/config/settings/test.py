from .base import *

# Testing-specific key
SECRET_KEY = "x-8r)c(97bk5z*i36(km!2)9yjizawo-+m77on2k!b1(4k+-0h"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
