#!/bin/bash

set -eo pipefail

log() {
    message="$1"
    printf "[$(date "+%d-%b-%Y %H:%M:%S")] ${message} \n"
    unset message
}

[[ -f .env.linux ]] && (source .env.linux ) || (echo .env.linux not found)

: ${DJANGO_SETTINGS_MODULE?}

# Name of the application
NAME=$(echo $DJANGO_SETTINGS_MODULE|sed 's/.settings$//g')

# the user to run as
USER=`whoami`

# the group to run as
GROUP=${USER}

# Django project directory
DJANGODIR=${DJANGODIR}

# we will communicte using this unix socket
SOCKFILE=/run/lock/${NAME}.gunicorn.sock

# how many worker processes should Gunicorn spawn
NUM_WORKERS=1

# Gunicorn timeout
TIME_OUT=120

#Gunicorn log file
LOG_FILE=/tmp/${NAME}.gunicorn.log

# which settings file should Django use
DJANGO_SETTINGS_MODULE=${NAME}.settings

# WSGI module name
DJANGO_WSGI_MODULE=${NAME}.wsgi

APP_PORT=${APP_PORT:-8000}

cd ${DJANGODIR}
log "DJANGODIR: ${DJANGODIR}"
log "SOCKFILE: ${SOCKFILE}"
log "NUM_WORKERS: ${NUM_WORKERS}"
log "NAME: ${NAME}"
log "APP_PORT: ${APP_PORT}"
log "Starting ${NAME} as `whoami`"

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)

test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

python3 manage.py wait-for-redis
python3 manage.py wait-for-db

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py initiateadmin

python3 manage.py collectstatic --noinput

# python3 manage.py runserver 0:8000
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=0.0.0.0:8000 \
    --log-level=${LOG_LEVEL} \
    --timeout=${TIME_OUT} \
    --log-file=- \
    --reload

