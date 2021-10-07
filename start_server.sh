#!/bin/sh
python manage.py migrate --no-input
python manage.py collectstatic --no-input

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python manage.py createsuperuser --no-input
fi

gunicorn acm_web_site.wsgi --bind 0.0.0.0:8010 --workers 3 &
nginx -g 'daemon off;'
