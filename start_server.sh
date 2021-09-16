#!/usr/bin/env bash
# start_server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd acm_web_site; python manage.py createsuperuser --no-input)
fi
(cd acm_web_site; gunicorn acm_web_site.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"