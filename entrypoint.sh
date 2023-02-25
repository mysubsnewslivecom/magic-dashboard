#!/bin/bash

set -euo pipefail

source /vault/secrets/config

log() {
    message="$1"
    printf "[$(date "+%d-%b-%Y %H:%M:%S")] ${message} \n"
    unset message
}

# Name of the application
NAME=${NAME?}

# the user to run as
USER=`whoami`

# the group to run as
GROUP=${USER}

# Django project directory
DJANGODIR=/${NAME}

# we will communicte using this unix socket
SOCKFILE=/run/lock/${NAME}.gunicorn.sock

# how many worker processes should Gunicorn spawn
NUM_WORKERS=${NUM_WORKERS?}

# Gunicorn timeout
TIME_OUT=120

#Gunicorn log file
LOG_FILE=/tmp/${NAME}.gunicorn.log

# which settings file should Django use
DJANGO_SETTINGS_MODULE=${NAME}.settings

# WSGI module name
DJANGO_WSGI_MODULE=${NAME}.wsgi

mkdir -pv ${DJANGODIR}
# chown ${USER}:${GROUP} ${DJANGODIR}
cd ${DJANGODIR}
log "DJANGODIR: ${DJANGODIR}"
log "SOCKFILE: ${SOCKFILE}"
log "NUM_WORKERS: ${NUM_WORKERS}"
log "NAME: ${NAME}"
log "DJANGO_PORT: ${DJANGO_PORT?}"
log "LOG_LEVEL: ${LOG_LEVEL?}"
log "Starting ${NAME} as `whoami`"

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)

test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

# Activate the virtual environment
source ${VIRTUAL_ENV}/bin/activate

# Start your Django Unicorn# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

# python3 manage.py wait-for-redis
# python3 manage.py wait-for-db

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py initiateadmin

python3 manage.py collectstatic --noinput

python3 manage.py runserver 0.0.0.0:${DJANGO_PORT}

# exec gunicorn ${DJANGO_WSGI_MODULE}:application \
#     --name $NAME \
#     --workers $NUM_WORKERS \
#     --user=$USER --group=$GROUP \
#     --bind=0.0.0.0:${DJANGO_PORT} \
#     --log-level=${LOG_LEVEL} \
#     --timeout=${TIME_OUT} \
#     --log-file=- \
#     --reload

