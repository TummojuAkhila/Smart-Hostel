from django.contrib import admin
from .models import Room, Payment, Complaint, Visitor, Announcement, Feedback, Attendance, FoodMenu

admin.site.site_header = "Smart Hostel Administration"
admin.site.site_title = "Smart Hostel Admin"
admin.site.index_title = "Hostel Management Admin"

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "room_type", "capacity", "price", "is_available", "assigned_to")
    list_filter = ("room_type", "is_available")
    search_fields = ("number",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "due_date", "paid", "transaction_id")
    list_filter = ("paid",)
    search_fields = ("user__username", "transaction_id")

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("subject", "user", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("subject", "user__username")

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visitor_name", "user", "visit_date", "approved")
    list_filter = ("approved",)
    search_fields = ("visitor_name", "user__username")

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "active", "created_at")
    list_filter = ("active",)
    search_fields = ("title",)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "created_at")
    search_fields = ("user__username",)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "present")
    list_filter = ("present",)
    search_fields = ("user__username",)

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ("meal_type", "dish_name", "date", "is_available")
    list_filter = ("meal_type", "date", "is_available")
    search_fields = ("dish_name",)
