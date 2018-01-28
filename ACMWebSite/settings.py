import os
from os import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '40u@e4hyjwj!8kn5h^b48w_h-!+yvy0r^bb9k)zbsc5p*!80ra'

# TODO Turn off in production
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'WebSite.apps.WebsiteConfig',
	'markdown_deux',
	'django_extensions',
	'rest_framework',
	'corsheaders'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'ACMWebSite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, "templates"),
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'debug': True,
		},
	},
]

WSGI_APPLICATION = 'ACMWebSite.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': environ.get('DATABASE_NAME', 'namedb'),
		'USER': environ.get('DATABASE_USER', 'userdb'),
		'PASSWORD': environ.get('DATABASE_PASSWORD', 'passworddb'),
		'HOST': environ.get('DATABASE_HOST', '127.0.0.1'),
		'PORT': environ.get('DATABASE_PORT', 'port')
	}
}

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME':
			'django.contrib.auth.password_validation'
			'.UserAttributeSimilarityValidator',
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

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static")
]

# Archivos multimedia.
MEDIA_ROOT = os.path.join(BASE_DIR, 'WebSite/static/media')
MEDIA_URL = '/media/'

EMAIL_HOST = environ.get('EMAIL_HOST', 'email_host')
EMAIL_PORT = environ.get('EMAIL_PORT', 'email_port')
EMAIL_USE_TLS = environ.get('EMAIL_USE_TLS', 'email_use_tls')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'email')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', 'password')
