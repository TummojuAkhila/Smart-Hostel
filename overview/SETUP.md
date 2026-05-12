# Smart Hostel Management System - Setup Guide

## ✅ Project Complete!

Your Django-based Smart Hostel Management System is ready to use. Follow these steps to get started:

---

## 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual Environment

---

## 🚀 Quick Start

### Step 1: Navigate to Project Directory
```bash
cd "c:\Users\Anand sai\Desktop\smart hostel stay"
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
```bash
# On Windows (Command Prompt):
.\venv\Scripts\activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Linux/Mac:
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 6: Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account:
- Username: (e.g., "admin")
- Email: (e.g., "admin@hostel.com")
- Password: (Create a strong password)

### Step 7: Run Development Server
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
```

---

## 🌐 Accessing the System

### Main Application
- **Home**: http://localhost:8000/
- **Login**: http://localhost:8000/login/
- **Register**: http://localhost:8000/register/

### Admin Panel
- **Django Admin**: http://localhost:8000/admin/
- **Admin Dashboard**: http://localhost:8000/admin-dashboard/
- **Tenant Dashboard**: http://localhost:8000/tenant-dashboard/

---

## 👥 Test Accounts

### Admin Account (Created with `createsuperuser`)
- Role: Hostel Owner/Admin
- Access: Full system management
- Dashboard: /admin-dashboard/

### Sample Tenant Account (Create via Registration)
1. Go to http://localhost:8000/register/
2. Enter username, email, and password
3. Login to access tenant features

---

## 📊 Database Setup

The system includes the following models:
- Users (with Admin/Tenant roles)
- Rooms (with allocation)
- Payments (fee tracking)
- Complaints (status tracking)
- Visitors (approval workflow)
- Announcements
- Feedback (with ratings)
- Attendance (optional tracking)
- FoodMenu (daily meal management)

All tables are automatically created during migration.

---

## 🔑 Key Features Overview

### Admin Features
1. **Room Management** - Allocate rooms to tenants
2. **Payment Management** - Manually add and update fees
3. **Complaint Management** - Track and update complaint status
4. **Announcements** - Create and manage hostel updates
5. **Visitor Requests** - Approve/reject visitor access
6. **Food Menu** - Update daily menu items

### Tenant Features
1. **Dashboard** - Quick overview of status
2. **Payments** - View pending fees
3. **Complaints** - Submit and track issues
4. **Visitors** - Request visitor approval
5. **Announcements** - View hostel updates
6. **Food Menu** - Check daily meals
7. **Feedback** - Submit ratings and feedback

---

## 📂 Important Files

- `manage.py` - Django management commands
- `requirements.txt` - Project dependencies
- `smart_hostel/settings.py` - Configuration
- `hostel/models.py` - Database models
- `hostel/views.py` - Application logic
- `hostel/forms.py` - Form definitions
- `hostel/templates/` - HTML templates
- `FEATURES.md` - Comprehensive feature documentation

---

## ⚙️ Configuration Notes

### Database
- Default: SQLite (db.sqlite3)
- For production, use PostgreSQL or MySQL
- Edit `smart_hostel/settings.py` to change database

### Static Files
- CSS files: `hostel/static/hostel/css/`
- Images: `hostel/static/hostel/images/`
- Run `python manage.py collectstatic` for production

### Email (Optional)
To enable email notifications, update `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

---

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

---

## 📱 API Endpoints

### Get All Rooms (JSON)
```
GET http://localhost:8000/api/rooms/
```

### Get Active Announcements (JSON)
```
GET http://localhost:8000/api/announcements/
```

---

## 🛠️ Common Commands

### Create superuser
```bash
python manage.py createsuperuser
```

### Create a new app
```bash
python manage.py startapp appname
```

### Check for errors
```bash
python manage.py check
```

### Reset migrations (⚠️ Warning: Clears data)
```bash
python manage.py migrate hostel zero
python manage.py migrate
```

### Clear cache
```bash
python manage.py clear_cache
```

---

## 🐛 Troubleshooting

### Issue: Module not found
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Port 8000 already in use
**Solution**: Use a different port
```bash
python manage.py runserver 8001
```

### Issue: Database errors
**Solution**: Rerun migrations
```bash
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic --noinput
```

---

## 📚 Documentation

For comprehensive feature details, see: `FEATURES.md`

---

## 🔒 Security Recommendations

For Production Deployment:
1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure random value
3. Use environment variables for sensitive data
4. Enable HTTPS with SSL certificate
5. Use PostgreSQL instead of SQLite
6. Set up proper backup strategy
7. Configure ALLOWED_HOSTS properly

---

## 📞 Support

For issues or feature requests, refer to the code comments and docstrings throughout the project.

---

## ✨ Next Steps

1. Create test data using the admin panel
2. Explore all features through the dashboards
3. Customize styling in `hostel/static/hostel/css/style.css`
4. Modify templates as needed
5. Set up email integration for notifications
6. Deploy to production when ready

---

**Happy Hostel Management! 🏠**

Version: 1.0  
Last Updated: May 2026
