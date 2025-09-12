🏋️‍♂️ Fitness Tracker API

A Django REST Framework API that allows users to track their fitness activities, log workouts, and monitor progress.
This project was built as part of the ALX Software Engineering Capstone.

📖 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Example Request](#example-request)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Author](#author)


# About the Project

The Fitness Tracker API helps users log and manage their workouts. Each user can:

Record activities (running, cycling, etc.)

Track workout duration and distance

Add notes for context (e.g., “Morning run at the park”)

Securely access only their own data

This project addresses the problem of personal fitness tracking by providing a backend system that can later be integrated with mobile or web frontends.

# Features

🔑 User Authentication (login, registration)

📋 CRUD Operations for fitness activities

🔒 User-specific access (each user sees only their activities)

🌐 REST API endpoints powered by Django REST Framework

# Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (default) → easily switchable to PostgreSQL/MySQL

Authentication: Django auth / JWT (planned)

Deployment: Render (or your chosen host)

# Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/okoli240/Alx_Capstone_FitnessTrackerAPI.git

cd Alx_Capstone_FitnessTrackerAPI/fitness_tracker_api

2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Create a Superuser
python manage.py createsuperuser

6️⃣ Start Development Server
python manage.py runserver

# API Endpoints
Method	Endpoint	Description
POST	/api/auth/register/	Register new user
POST	/api/auth/login/	Login and get token
GET	/api/activities/	List all activities (user-specific)
POST	/api/activities/	Create new activity
GET	/api/activities/{id}/	Retrieve single activity
PUT	/api/activities/{id}/	Update an activity
DELETE	/api/activities/{id}/	Delete an activity
# Authentication

Currently uses Django’s built-in auth system

Planned upgrade: JWT Authentication with djangorestframework-simplejwt

Example (after JWT is added):

Authorization: Bearer <your_token_here>

# Example Request
Create Activity

POST /api/activities/

{
  "activity_type": "Running",
  "duration": 45,
  "distance": 10,
  "date": "2025-08-31",
  "notes": "Morning run at the park"
}

# Deployment

## Deployment

The project is currently running locally. Deployment options include Render, Railway, or Heroku.


# Future Improvements

🔐 Add JWT authentication (djangorestframework-simplejwt)

📊 Add charts & analytics (distance trends, calories burned)

💻 Add frontend (React/Next.js) to visualize activities

📱 Mobile integration (Flutter/React Native)

# Author 

Chibunkem Okoli

GitHub: [okoli240](https://github.com/okoli240)  

LinkedIn: [Chibunkem Okoli](https://www.linkedin.com/in/chibunkem-okoli-12917a164)