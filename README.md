# Django Blog Website

## Introduction
This is a fully functional blog website built using Django, a high-level Python web framework. The blog allows users to create, edit, and delete posts, as well as interact with content through comments and likes.

## Features
- User authentication (signup, login, logout)
- Create, read, update, and delete (CRUD) blog posts
- Comments on posts
- Like functionality for posts
- Responsive design with HTML, CSS, and Bootstrap
- Pagination for posts
- SEO-friendly URLs
- Admin panel for managing posts and users

## Technologies Used
- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default), can be switched to PostgreSQL or MySQL
- **Other Tools**: Django Admin, Django Templates, Django Authentication

## Installation

### Prerequisites
- Python (>=3.8)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (to access Django Admin panel):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Configuration
- Update `settings.py` for database configurations.
- Modify `STATIC_URL` and `MEDIA_URL` for static and media file handling.
- Configure environment variables for security-related settings.
