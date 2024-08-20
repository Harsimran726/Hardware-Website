#!/bin/bash

set -e

# Replace with your project path
PROJECT_DIR="project"

# Activate virtual environment (if used)

cd "project"


python3 manage.py collectstatic --noinput

echo "Static files collected successfully!"