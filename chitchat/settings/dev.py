from .base import *
from decouple import config


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chitchatdb',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}
