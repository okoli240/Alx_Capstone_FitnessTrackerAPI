# Fitness Tracker API

## Features
- User management with Django's built-in User model.
- CRUD operations for fitness activities.
- REST API endpoints for activities using Django REST Framework.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
