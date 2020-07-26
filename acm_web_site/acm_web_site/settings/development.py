from .common import *

DEBUG = TEMPLATE_DEBUG = True

THIRD_PARTY_APPS = THIRD_PARTY_APPS + [
    'django_extensions',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INTERNAL_IPS = ('127.0.0.1',)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
