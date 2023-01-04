ARG IMAGE_NAME=python
ARG IMAGE_TAG=3.10-alpine

ARG DJANGO_PORT=9000
ARG GUNICORN_WORKERS=1

# pull official base image
FROM ${IMAGE_NAME}:${IMAGE_TAG}

# LABEL about the custom image
LABEL maintainer="linux@ubuntu-master"
LABEL version="0.1"
LABEL description="This is custom Docker Image for the django app."

RUN mkdir -pv /app/requirements

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV USER linux
ENV GROUP linux
ENV APP_NAME magic-dashboard
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

COPY pyproject.toml /app

# install dependencies
RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base bash \
    && python -m venv /env \
    && /env/bin/pip install --upgrade poetry \
    && /env/bin/poetry install -C /app \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

COPY . /app

RUN mkdir -p /var/www/static/

EXPOSE ${DJANGO_PORT}

VOLUME /app/run/

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D ${USER}

CMD [ "/env/bin/python3", "manage.py", "runserver", "0.0.0.0:9000" ]
