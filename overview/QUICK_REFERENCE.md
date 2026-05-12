# Admin & Tenant Feature Quick Reference

## 🎯 Admin Dashboard - Quick Navigation

### Management Panels (All in one place)

| Feature | URL | Purpose |
|---------|-----|---------|
| **Room Management** | `/rooms/` | View all rooms and allocate to tenants |
| **Payment Management** | `/manage-payments/` | Add/update/delete payment records |
| **Complaint Management** | `/manage-complaints/` | Track and update complaint status |
| **Announcements** | `/manage-announcements/` | Create/edit/delete announcements |
| **Visitor Requests** | `/manage-visitors/` | Approve/reject visitor requests |
| **Food Menu** | `/manage-food-menu/` | Add/update/delete daily menu items |

---

## 📋 Admin Workflows

### Adding a Payment Manually
1. Go to `/manage-payments/`
2. Fill in the form:
   - Select tenant
   - Enter amount
   - Set due date
   - Add transaction ID (optional)
   - Check "Paid" if payment received
3. Click "Create Payment"

### Creating an Announcement
1. Go to `/manage-announcements/`
2. Enter title and message
3. Check "Active" to make it visible
4. Click "Create Announcement"

### Managing Food Menu
1. Go to `/manage-food-menu/`
2. Select meal type (Breakfast/Lunch/Dinner/Snacks)
3. Enter dish name and description
4. Set date
5. Check "Available"
6. Click "Add to Menu"

### Allocating a Room
1. Go to `/rooms/`
2. Click "Allocate" on desired room
3. Select tenant username
4. Click "Allocate"

### Updating Complaint Status
1. Go to `/manage-complaints/`
2. Click "Update Status" on complaint
3. Change status to:
   - Open (New complaint)
   - In Progress (Being worked on)
   - Resolved (Issue fixed)
4. Click "Update Status"

### Approving Visitor Requests
1. Go to `/manage-visitors/`
2. Click "Approve" for pending requests
3. Request will be marked as approved

---

## 👤 Tenant Dashboard - Features

### Quick Actions (Available on Dashboard)
- **Raise Complaint** - Go to complaints page
- **Visitor Request** - Submit visitor approval request
- **View Payments** - Check pending fees
- **View Menu** - Check daily food menu

### What Tenants Can Do

| Feature | Purpose |
|---------|---------|
| **My Room** | See assigned room details |
| **Pending Fees** | View amount and due date |
| **My Complaints** | Submit issues and track status |
| **Visitor Requests** | Request visitor approval |
| **Food Menu** | Browse daily meals by type |
| **Announcements** | See hostel updates |
| **Feedback** | Rate services (1-5 stars) |

---

## 🔄 Data Relationships

### Room → User
- One room allocated to one tenant
- Admin controls allocation
- Rooms show as occupied/vacant

### Payment → User
- One user can have multiple payments
- Each payment has due date and status
- Admin manually creates/updates

### Complaint → User
- User submits complaint
- Admin updates status
- User tracks progress

### Visitor → User
- Tenant requests visitor approval
- Visitor has date and purpose
- Admin approves/rejects

### Announcement → All Users
- Admin creates announcement
- All tenants see it
- Can be activated/deactivated

### FoodMenu → All Users
- Admin adds menu items
- Organized by date and meal type
- Tenants view available meals

---

## 📊 Dashboard Statistics

### Admin Dashboard Shows:
- Total rooms count
- Available (vacant) rooms count
- Total registered tenants
- Open complaints count
- Pending visitor requests count
- Pending payments count

### Tenant Dashboard Shows:
- My assigned room
- My pending fees
- Latest announcements
- Today's food menu preview

---

## 🎨 UI Components

### Forms Used
- **Payment Form**: Amount, tenant, date, transaction ID, paid status
- **Announcement Form**: Title, message, active status
- **Complaint Form**: Subject, detailed message
- **Visitor Request Form**: Visitor name, visit date, purpose
- **Food Menu Form**: Meal type, dish name, description, date, availability
- **Feedback Form**: Message, rating (1-5)

### Common Actions
- ✏️ **Edit** - Update existing record
- 🗑️ **Delete** - Remove record permanently
- ✓ **Approve** - Mark as approved
- 📅 **Update Status** - Change complaint status
- 👁️ **View** - See full details

---

## 📱 Responsive Design

All pages are mobile-responsive:
- Desktop: Full width with sidebar
- Tablet: Adjusted layout
- Mobile: Stack vertically

---

## ⚡ Pro Tips for Admins

1. **Bulk Operations**: Use Django admin (/admin/) for bulk editing
2. **Export Data**: Copy payment data for accounting
3. **Search**: Use browser find (Ctrl+F) in tables
4. **Date Picker**: Click date fields for calendar popup
5. **Status Badges**: Green = Active/Approved, Red = Open/Pending

---

## 🔐 Access Control

### Admin Only Pages
- Room allocation
- Payment management
- Complaint updates
- Announcements
- Visitor approvals
- Food menu management

### Tenant Pages
- Personal dashboard
- My room details
- My payments view
- My complaints
- My visitor requests
- View menu/announcements

---

## 📝 Example Workflows

### Workflow 1: New Tenant Onboarding
1. Admin creates account (OR tenant self-registers)
2. Admin allocates room to tenant
3. Admin creates first payment record
4. Tenant logs in and sees dashboard
5. Tenant accepts terms and settles in

### Workflow 2: Complaint Resolution
1. Tenant submits complaint
2. Admin updates status to "In Progress"
3. Admin resolves issue
4. Admin marks status as "Resolved"
5. Tenant sees resolved status

### Workflow 3: Visitor Management
1. Tenant submits visitor request
2. Admin reviews request
3. Admin clicks "Approve"
4. Tenant sees approved status
5. Visitor can come on that date

### Workflow 4: Food Menu Setup
1. Admin goes to food menu page
2. Admin adds breakfast items
3. Admin adds lunch items
4. Admin adds dinner items
5. Tenants see menu on dashboard

---

## 🚀 Performance Tips

- Keep announcements concise
- Archive old complaints
- Update menu weekly
- Monitor payment status regularly
- Allocate rooms efficiently

---

**All features are now live and ready to use!** 🎉
