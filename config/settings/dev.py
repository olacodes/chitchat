from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chitchatdb',
        'HOST': 'localhost',
        'USER': config('DBUSER'),
        'PASSWORD': config('DBPASSWD')
    }
}
