"""
WSGI config for ACMWebSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import os

from django.core.wsgi import get_wsgi_application

from .settings.common import SITE_NAME

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    "{}.{}.settings.production".format(SITE_NAME, SITE_NAME)
)

application = get_wsgi_application()

