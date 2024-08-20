#!/bin/bash

set -e

# Replace with your project path
PROJECT_DIR="project"
python3 -m venv my_env
source my_env/bin/activate
# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt

# Activate virtual environment (if used)
source my_env/Scripts/activate  # Windows
# source my_env/bin/activate     # macOS/Linux

cd "$PROJECT_DIR"

python3 manage.py collectstatic --noinput

echo "Static files collected successfully!"
