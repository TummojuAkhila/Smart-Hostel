# Smart Hostel Management System - Complete Feature Documentation

## Overview
A comprehensive Django-based hostel management system with separate dashboards for Admin (Hostel Owner) and Tenant (User) roles.

---

## 🔹 User Roles

### Admin (Hostel Owner)
- Full system access and management capabilities
- Dashboard with comprehensive analytics
- Ability to manage all features

### Tenant (Hostel User)
- Limited access to personal information and requests
- Ability to submit complaints, visitor requests, and feedback
- View assigned room, payments, announcements, and food menu

---

## 🔹 Authentication System
- Django built-in authentication
- User registration with email
- Secure login/logout system
- Role-based access control (Admin vs Tenant)

---

## 🔹 Admin Dashboard
### Analytics & Overview
- **Total Rooms**: Display count of all rooms
- **Available Rooms**: Count of vacant rooms
- **Total Tenants**: Number of registered tenants
- **Open Complaints**: Count of unresolved complaints
- **Pending Visitor Requests**: Requests awaiting approval
- **Pending Payments**: Count of unpaid fees

### Management Modules
1. **Room Management**
   - View all rooms
   - Allocate rooms to tenants
   - Track room availability and assignment status

2. **Payment Management**
   - Create new payment records manually
   - Update existing payment details
   - Mark payments as paid/unpaid
   - Delete payment records
   - Track payment history

3. **Complaint Management**
   - View all complaints from tenants
   - Update complaint status (Open → In Progress → Resolved)
   - Track complaint resolution timeline

4. **Announcements Management**
   - Create new announcements
   - Edit announcements
   - Activate/deactivate announcements
   - Delete announcements
   - View all announcements with timestamps

5. **Visitor Request Management**
   - View all visitor requests
   - Approve/reject visitor requests
   - Track visitor visit dates and purposes

6. **Food Menu Management**
   - Add new menu items for different meal types:
     - Breakfast
     - Lunch
     - Dinner
     - Snacks
   - Specify date and dish description
   - Mark items as available/unavailable
   - Update or delete menu items
   - View complete food menu

---

## 🔹 Tenant Dashboard
### Quick Overview
- **Assigned Room**: Display room number, type, capacity, and price
- **Fees to Pay**: Show pending payments with due dates
- **Latest Announcements**: Recent hostel updates
- **Food Menu Preview**: Latest meal options

### Tenant Features

1. **Room View**
   - See assigned room details
   - View room specifications

2. **Payment Tracking**
   - View pending fees
   - Track payment history
   - See payment due dates

3. **Complaint System**
   - Raise new complaints
   - View complaint history
   - Track complaint status updates

4. **Visitor Requests**
   - Submit visitor request with:
     - Visitor name
     - Visit date
     - Purpose of visit
   - View request status (Approved/Pending)

5. **Announcements**
   - View active announcements
   - Get latest hostel updates

6. **Food Menu**
   - View daily food menu
   - Browse meals by type:
     - Breakfast
     - Lunch
     - Dinner
     - Snacks
   - See dish descriptions

7. **Feedback System**
   - Submit feedback
   - Rate hostel services (1-5 stars)
   - View submission history

---

## 🔹 Database Models

### User Model
- Django built-in User model extended with is_staff for role differentiation

### Room Model
```
- number (Unique identifier)
- room_type (Single/Double/Suite)
- capacity (Number of occupants)
- price (Monthly rent in decimal)
- is_available (Boolean availability flag)
- assigned_to (ForeignKey to User)
```

### Payment Model
```
- user (ForeignKey)
- amount (Decimal amount)
- due_date (Date field)
- paid (Boolean status)
- transaction_id (String for payment reference)
- created_at (Auto-timestamp)
```

### Complaint Model
```
- user (ForeignKey)
- subject (Complaint title)
- message (Detailed description)
- status (Open/In Progress/Resolved)
- created_at (Auto-timestamp)
- updated_at (Auto-update timestamp)
```

### Visitor Model
```
- user (ForeignKey)
- visitor_name (Name of visitor)
- visit_date (Date of visit)
- purpose (Purpose of visit)
- approved (Boolean approval status)
- created_at (Auto-timestamp)
```

### Announcement Model
```
- title (Announcement title)
- message (Full message content)
- active (Boolean status)
- created_at (Auto-timestamp)
```

### Feedback Model
```
- user (ForeignKey)
- message (Feedback text)
- rating (1-5 star rating)
- created_at (Auto-timestamp)
```

### Attendance Model
```
- user (ForeignKey)
- date (Date of attendance)
- present (Boolean status)
```

### FoodMenu Model
```
- meal_type (Breakfast/Lunch/Dinner/Snacks)
- dish_name (Name of dish)
- description (Dish description)
- date (Date of menu)
- is_available (Boolean availability)
- created_at (Auto-timestamp)
```

---

## 🔹 API Endpoints (JSON API)

### Public Endpoints
- `/api/rooms/` - Get all available rooms with details
- `/api/announcements/` - Get active announcements

---

## 🔹 Frontend Features

### Responsive Design
- Built with Bootstrap 5
- Mobile-friendly UI
- Adaptive layouts

### Forms & Validation
- Server-side validation using Django forms
- User-friendly error messages
- Auto-complete and date pickers

### Navigation
- Top navbar with contextual links
- Dashboard quick links
- Breadcrumb navigation

---

## 🔹 Advanced Features

1. **Role-Based Access Control (RBAC)**
   - Admin-only pages protected by @staff_required decorator
   - Tenant-specific data filtering
   - Permission-based view rendering

2. **Notifications System**
   - Django messages framework for feedback
   - Success/error/warning alerts
   - Toast-style notifications

3. **Data Filtering & Search**
   - Admin panel filters by status, type, date
   - Quick search capabilities

4. **Activity Logging**
   - Automatic timestamps on all records
   - Created/updated tracking

---

## 🔹 Setup & Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment

### Installation Steps
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Access Points
- Admin Panel: http://localhost:8000/admin/
- Home: http://localhost:8000/
- Login: http://localhost:8000/login/
- Register: http://localhost:8000/register/

---

## 🔹 URL Routing

### Public URLs
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout

### Admin URLs
- `/admin-dashboard/` - Admin dashboard
- `/rooms/` - Room management
- `/manage-payments/` - Payment management
- `/manage-announcements/` - Announcements management
- `/manage-complaints/` - Complaints management
- `/manage-visitors/` - Visitor requests management
- `/manage-food-menu/` - Food menu management
- `/update-payment/<id>/` - Edit payment
- `/update-announcement/<id>/` - Edit announcement
- `/update-complaint/<id>/` - Update complaint status
- `/update-food-menu/<id>/` - Edit food menu item
- `/allocate-room/<id>/` - Allocate room to tenant

### Tenant URLs
- `/tenant-dashboard/` - Tenant dashboard
- `/payments/` - View payments
- `/complaints/` - Submit/view complaints
- `/announcements/` - View announcements
- `/visitor-request/` - Submit/view visitor requests
- `/feedback/` - Submit feedback
- `/view-food-menu/` - View food menu
- `/approve-visitor/<id>/` - Approve visitor request

---

## 🔹 File Structure
```
smart_hostel_stay/
├── manage.py
├── requirements.txt
├── README.md
├── smart_hostel/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── hostel/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── __init__.py
│   ├── migrations/
│   ├── templates/hostel/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard_admin.html
│   │   ├── dashboard_tenant.html
│   │   ├── rooms.html
│   │   ├── payments.html
│   │   ├── manage_payments.html
│   │   ├── update_payment.html
│   │   ├── complaints.html
│   │   ├── manage_complaints.html
│   │   ├── update_complaint_status.html
│   │   ├── announcements.html
│   │   ├── manage_announcements.html
│   │   ├── update_announcement.html
│   │   ├── visitor_requests.html
│   │   ├── manage_visitors.html
│   │   ├── feedback.html
│   │   ├── manage_food_menu.html
│   │   ├── update_food_menu.html
│   │   ├── view_food_menu.html
│   │   └── allocate_room.html
│   └── static/hostel/css/
│       └── style.css
```

---

## 🔹 Security Features
- CSRF protection on all forms
- Password hashing with Django's authentication system
- SQL injection prevention via ORM
- Login required decorators on all protected views
- Role-based access control

---

## 🔹 Future Enhancements
- Email notifications for payments and approvals
- SMS alerts for complaints
- Advanced analytics and reporting
- Inventory management for food items
- Maintenance request system
- Online payment gateway integration (Razorpay/Stripe)
- Mobile app integration via REST API
- Multi-language support

---

**Version**: 1.0  
**Last Updated**: May 2026  
**License**: MIT
