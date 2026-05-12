# Smart Hostel Management System

A Django-based hostel management system supporting tenants and admin owners.

## Features
- User authentication with Django auth
- Role-based dashboards for Admin and Tenant
- Room allocation and vacancy management
- Fee & payment tracking
- Complaint system with status tracking
- Announcements and visitor request workflows
- Feedback collection
- Basic JSON API endpoints for integration

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Notes
- Admin users should be marked with `is_staff=True`.
- Tenant users register via the registration form.
- Use the Django admin site to manage rooms, payments, and users.
