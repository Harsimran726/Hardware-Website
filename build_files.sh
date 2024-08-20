#!/bin/bash

set -e

# Replace with your project path
PROJECT_DIR="project"

# Activate virtual environment (if used)
source my_env/Scripts/activate

cd "project"

python manage.py collectstatic --noinput

echo "Static files collected successfully!"