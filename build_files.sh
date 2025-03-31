#!/bin/bash
echo "Installing dependencies..."
python -m pip install -r requirements.txt
echo "Running collectstatic..."
python manage.py collectstatic --noinput