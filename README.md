Django Blog Website

Introduction

This is a fully functional blog website built using Django, a high-level Python web framework. The blog allows users to create, edit, and delete posts, as well as interact with content through comments and likes.

Features

User authentication (signup, login, logout)

Create, read, update, and delete (CRUD) blog posts

Comments on posts

Like functionality for posts

Responsive design with HTML, CSS, and Bootstrap

Pagination for posts

SEO-friendly URLs

Admin panel for managing posts and users

Technologies Used

Backend: Django, Django ORM

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite (default), can be switched to PostgreSQL or MySQL

Other Tools: Django Admin, Django Templates, Django Authentication

Installation

Prerequisites

Python (>=3.8)

pip (Python package manager)

Virtual environment (optional but recommended)

Steps

Clone the repository:

git clone https://github.com/yourusername/django-blog.git
cd django-blog

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create a superuser (to access Django Admin panel):

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open the application in your browser:
