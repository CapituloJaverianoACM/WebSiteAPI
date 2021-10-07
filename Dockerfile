# Dockerfile

FROM python:alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE=acm_web_site.settings.production

# Install Deps on alpine
RUN apk add postgresql-dev nginx libjpeg-turbo-dev
RUN apk add --virtual .deps gcc g++ python3-dev build-base zlib-dev 

# Copy requirements
COPY ./requirements/prod.txt .
COPY ./requirements/common.txt .
RUN pip install -r prod.txt

RUN apk del .deps

COPY ./nginx.conf /etc/nginx/nginx.conf

# Copy Django files
COPY ./acm_web_site /app

WORKDIR /app

COPY ./start_server.sh /
EXPOSE 8080
ENTRYPOINT ["sh", "/start_server.sh"]

