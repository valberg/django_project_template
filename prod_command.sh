#!/bin/sh

cd src
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 --workers 1 --timeout 60 project.wsgi
