from decimal import Decimal
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Complaint, Visitor, Feedback, FoodMenu, Payment, Announcement, Room, Poll


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter phone number"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["subject", "message"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class VisitorRequestForm(forms.ModelForm):
    visit_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}))

    class Meta:
        model = Visitor
        fields = ["visitor_name", "visit_date", "purpose"]
        widgets = {
            "visitor_name": forms.TextInput(attrs={"class": "form-control"}),
            "purpose": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["message", "rating"]
        widgets = {
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5}),
        }


class FoodMenuForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}))

    class Meta:
        model = FoodMenu
        fields = ["meal_type", "dish_name", "description", "date", "is_available"]
        widgets = {
            "meal_type": forms.Select(attrs={"class": "form-select"}),
            "dish_name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "is_available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class PaymentForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Payment
        fields = ["user", "amount", "paid_amount", "due_date", "paid", "transaction_id"]
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "paid_amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "Amount paid by tenant"}),
            "due_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "paid": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "transaction_id": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get("amount") or Decimal("0")
        paid_amount = cleaned_data.get("paid_amount") or Decimal("0")

        if paid_amount > amount:
            self.add_error("paid_amount", "Paid amount cannot exceed the total amount.")

        return cleaned_data


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "message", "active"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class PollForm(forms.ModelForm):
    options = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "One option per line"}),
        help_text="Enter one option per line for this poll.",
    )

    class Meta:
        model = Poll
        fields = ["title", "description", "is_admin_poll", "active"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "is_admin_poll": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None or self.instance.pk is None:
            self.fields["active"].initial = True


class TenantPollForm(PollForm):
    class Meta(PollForm.Meta):
        fields = ["title", "description", "active"]


class ComplaintStatusForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["status"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class RoomForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Room
        fields = ["number", "room_type", "capacity", "price", "is_available", "assigned_to"]
        widgets = {
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "room_type": forms.Select(attrs={"class": "form-select"}),
            "capacity": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "is_available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make assigned_to optional
        self.fields["assigned_to"].required = False
