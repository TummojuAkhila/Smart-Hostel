# Unit tests for hostel management system

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Room, Payment, Complaint, Visitor, Announcement, Feedback, Attendance, FoodMenu


class RoomModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(
            number="101",
            room_type="single",
            capacity=1,
            price=5000.00
        )

    def test_room_creation(self):
        self.assertEqual(self.room.number, "101")
        self.assertTrue(self.room.is_available)


class UserAuthTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin",
            password="admin123",
            is_staff=True
        )
        self.tenant = User.objects.create_user(
            username="tenant1",
            password="tenant123"
        )

    def test_admin_creation(self):
        self.assertTrue(self.admin.is_staff)

    def test_tenant_creation(self):
        self.assertFalse(self.tenant.is_staff)


class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tenant",
            password="pass123"
        )
        self.payment = Payment.objects.create(
            user=self.user,
            amount=5000.00,
            paid=False
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.amount, 5000.00)
        self.assertFalse(self.payment.paid)


class ComplaintModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tenant",
            password="pass123"
        )
        self.complaint = Complaint.objects.create(
            user=self.user,
            subject="Leaky tap",
            message="Water is leaking from tap",
            status="open"
        )

    def test_complaint_creation(self):
        self.assertEqual(self.complaint.subject, "Leaky tap")
        self.assertEqual(self.complaint.status, "open")


class FoodMenuModelTest(TestCase):
    def setUp(self):
        from datetime import date
        self.food = FoodMenu.objects.create(
            meal_type="lunch",
            dish_name="Biryani",
            date=date.today(),
            is_available=True
        )

    def test_food_menu_creation(self):
        self.assertEqual(self.food.dish_name, "Biryani")
        self.assertTrue(self.food.is_available)
