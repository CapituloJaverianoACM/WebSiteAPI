import os
import sys
from os import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'run', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'run', 'media')

sys.path.append(os.path.normpath(os.path.join(PROJECT_ROOT, 'apps')))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '40u@e4hyjwj!8kn5h^b48w_h-!+yvy0r^bb9k)zbsc5p*!80ra'
)

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'markdownx',
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
    'utils',
    'business.activities',
    'business.people',
    'business.information',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'acm_web_site.urls'
WSGI_APPLICATION = 'acm_web_site.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "../../../templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ]
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DATABASE_NAME', 'namedb'),
        'USER': environ.get('DATABASE_USER', 'userdb'),
        'PASSWORD': environ.get('DATABASE_PASSWORD', 'passworddb'),
        'HOST': environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': environ.get('DATABASE_PORT', '5432')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Bogota')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Archivos multimedia.
MEDIA_URL = '/media/'

EMAIL_HOST = environ.get('EMAIL_HOST', 'email_host')
EMAIL_PORT = environ.get('EMAIL_PORT', 'email_port')
EMAIL_USE_TLS = environ.get('EMAIL_USE_TLS', 'email_use_tls')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'email')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', 'password')

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# for production (only the front end server should be here)
"""CORS_ORIGIN_WHITELIST = [
    environ.get('REACT_JS_SERVER_IP', 'http://acmwebsite-service:'),
    'http://localhost:8000',
    'http://localhost:8080',
]"""
