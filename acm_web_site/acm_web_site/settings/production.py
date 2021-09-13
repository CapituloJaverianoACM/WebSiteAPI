from .common import *

TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'tmp'))

DEBUG = TEMPLATE_DEBUG = False
SESSION_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INTERNAL_IPS = ('127.0.0.1',)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROOT_URLCONF = 'acm_web_site.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static'),
]
