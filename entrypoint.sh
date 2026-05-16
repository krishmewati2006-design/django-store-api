#!/bin/sh 
python manage.py migrate
gunicorn store.wsgi