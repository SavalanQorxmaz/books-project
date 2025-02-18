#!/bin/bash

source ./.venv/Scripts/activate

sleep 1

# cd ./project || { echo "Not found!"; exit 1; }

 python ./project/manage.py runserver 