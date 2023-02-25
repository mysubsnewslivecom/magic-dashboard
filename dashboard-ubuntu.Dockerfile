ARG IMAGE_NAME=python
ARG IMAGE_TAG=slim-buster

ARG DJANGO_PORT=9000
ARG GUNICORN_WORKERS=1

# pull official base image
FROM --platform=linux/arm64/v8 ${IMAGE_NAME}:${IMAGE_TAG}
# FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# LABEL about the custom image
LABEL maintainer="linux@ubuntu-master"
LABEL version="0.1"
LABEL description="This is custom Docker Image for the django app."

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV USER linux
ENV GROUP linux
ENV HOME /home/${USER}
ENV C_FORCE_ROOT true
ENV APP_NAME /rotary_phone
ENV VIRTUAL_ENV /env
ENV PATH "${HOME}/.local/bin:${PATH}:/env/bin"
ENV TZ=UTC

RUN mkdir -pv ${APP_NAME}/requirements

# set work directory
WORKDIR ${APP_NAME}

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
    build-essential ca-certificates software-properties-common \
    libpq-dev && rm -rf /var/lib/apt/lists/* && \
    apt-get clean && apt-get autoremove -qy

# RUN apt-get install -y --no-install-recommends postgresql-client \
#     build-essential ca-certificates software-properties-common \
#     libpq-dev && rm -rf /var/lib/apt/lists/* && apt-get clean

RUN python3 -m venv ${VIRTUAL_ENV} && /env/bin/pip install --upgrade pip poetry

# RUN chown -R ${USER}:${GROUP} ${VIRTUAL_ENV} ${APP_NAME}

COPY pyproject.toml ${APP_NAME}/

RUN /env/bin/poetry install -C ${APP_NAME} --no-cache

COPY . ${APP_NAME}

RUN mkdir -p /var/www/static/

EXPOSE ${DJANGO_PORT}

VOLUME ${APP_NAME}/run/

# add and run as non-root user
# USER ${USER}

# RUN apt install gcc++


