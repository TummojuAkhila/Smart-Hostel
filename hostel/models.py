from decimal import Decimal
from django.conf import settings
from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="rooms")

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"Room {self.number} ({self.get_room_type_display()})"


class TenantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-due_date"]

    def __str__(self):
        return f"{self.user.username} - ₹{self.amount}"
    
    def get_remaining_amount(self):
        """Calculate remaining amount"""
        return self.amount - self.paid_amount
    
    remaining_amount = property(get_remaining_amount)


class Complaint(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="complaints")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} ({self.get_status_display()})"


class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="visitor_requests")
    visitor_name = models.CharField(max_length=200)
    visit_date = models.DateField()
    purpose = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-visit_date"]

    def __str__(self):
        return f"{self.visitor_name} for {self.user.username}"


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Feedback by {self.user.username}"


class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class FoodMenu(models.Model):
    MEAL_TYPES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snacks", "Snacks"),
    ]

    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    dish_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "meal_type"]
        unique_together = ("meal_type", "date", "dish_name")

    def __str__(self):
        return f"{self.get_meal_type_display()} - {self.dish_name} ({self.date})"


class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="polls")
    is_admin_poll = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def total_votes(self):
        return self.votes.count()


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.option_text} ({self.poll.title})"

    def vote_count(self):
        return self.votes.count()


class PollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes")
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="poll_votes")
    voted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("poll", "user")

    def __str__(self):
        return f"{self.user.username} voted for {self.option.option_text}"
