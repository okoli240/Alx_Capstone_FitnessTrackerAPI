🏋️‍♂️ Fitness Tracker API

A simple Django REST Framework API for tracking fitness activities. Users can log their workouts, track distance, and record notes.

🚀 Features

🔑 User Authentication using Django’s built-in User model

📋 CRUD operations for fitness activities (create, view, update, delete)

🌐 REST API endpoints powered by Django REST Framework

🔒 User-specific access (users can only see their own activities)

🛠️ Tech Stack

Django

Django REST Framework

SQLite (default, can be swapped for PostgreSQL/MySQL)

⚡ Setup Instructions

Clone the repository

git clone https://github.com/your-username/fitness-tracker-api.git
cd fitness-tracker-api


Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create a superuser (admin)

python manage.py createsuperuser


Start the development server

python manage.py runserver

📡 API Endpoints
Method	Endpoint	Description
GET	/api/activities/	List all activities (user-specific)
POST	/api/activities/	Create a new activity
GET	/api/activities/{id}/	Retrieve a single activity
PUT	/api/activities/{id}/	Update an activity
DELETE	/api/activities/{id}/	Delete an activity
🖼️ Example Request
POST /api/activities/
Content-Type: application/json

{
  "activity_type": "Running",
  "duration": 45,
  "distance": 10,
  "date": "2025-08-31",
  "notes": "Morning run at the park"
}

✅ Next Steps / Future Improvements

Add JWT authentication (using djangorestframework-simplejwt)

Add frontend (React/Next.js) to visualize activities

Add charts & analytics (total distance, calories burned, etc.)