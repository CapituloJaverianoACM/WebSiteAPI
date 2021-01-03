FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
&& rm -rf /var/lib/apt/lists/*
RUN mkdir -p /code && chown user:user /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements/prod.txt
RUN python acm_web_site/manage.py collectstatic --settings=acm_web_site.settings.production
#TODO: this is running with root because the permissions were denied for user
#USER user
VOLUME ["/code/acm_web_site/run"]
EXPOSE 8000
CMD ["uwsgi", "--ini", "acm_web_site/acm_web_site/uwsgi.ini"]