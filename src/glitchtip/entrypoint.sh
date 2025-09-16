#!/bin/bash

echo "Running migrations..."
./bin/run-migrate.sh

echo "Creating Django superuser..."
python manage.py createsuperuser --noinput

echo "Launching GlitchTip Web App..."
./bin/start.sh
