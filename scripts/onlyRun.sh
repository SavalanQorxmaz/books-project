#!/bin/bash



cd ./project || { echo "Not found!"; exit 1; }

python manage.py runserver 