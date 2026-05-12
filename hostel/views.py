from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .forms import (
    UserRegistrationForm, ComplaintForm, VisitorRequestForm, FeedbackForm,
    FoodMenuForm, PaymentForm, AnnouncementForm, ComplaintStatusForm, RoomForm
)
from .models import (
    Announcement, Complaint, Feedback, Payment, Room, Visitor, FoodMenu, Attendance,
    TenantProfile, Poll, PollOption, PollVote
)


def staff_required(view_func):
    return user_passes_test(lambda u: u.is_staff, login_url="login")(view_func)


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("admin_dashboard")
        return redirect("tenant_dashboard")
    return redirect("login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")
        messages.error(request, "Invalid credentials. Please try again.")
    return render(request, "hostel/login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.is_staff = False
        user.save()
        phone_number = form.cleaned_data.get("phone_number")
        TenantProfile.objects.create(user=user, phone_number=phone_number or "")
        messages.success(request, "Registration complete. You can now log in.")
        return redirect("login")
    return render(request, "hostel/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


@login_required
@staff_required
def admin_dashboard(request):
    total_rooms = Room.objects.count()
    available_rooms = Room.objects.filter(is_available=True).count()
    total_tenants = User.objects.filter(is_staff=False).count()
    pending_visitors = Visitor.objects.filter(approved=False, rejected=False).count()
    open_complaints = Complaint.objects.filter(status="open").count()
    pending_payments = Payment.objects.filter(paid=False).count()
    announcements = Announcement.objects.filter(active=True)[:5]
    
    context = {
        "total_rooms": total_rooms,
        "available_rooms": available_rooms,
        "total_tenants": total_tenants,
        "pending_visitors": pending_visitors,
        "open_complaints": open_complaints,
        "pending_payments": pending_payments,
        "announcements": announcements,
    }
    return render(request, "hostel/dashboard_admin.html", context)


@login_required
def tenant_dashboard(request):
    if request.user.is_staff:
        return redirect("admin_dashboard")
    assigned_rooms = Room.objects.filter(assigned_to=request.user)
    upcoming_payments = Payment.objects.filter(user=request.user, paid=False)
    active_announcements = Announcement.objects.filter(active=True)[:5]
    today_food = FoodMenu.objects.filter(is_available=True).order_by("-date", "meal_type")[:8]
    
    context = {
        "assigned_rooms": assigned_rooms,
        "upcoming_payments": upcoming_payments,
        "active_announcements": active_announcements,
        "today_food": today_food,
    }
    return render(request, "hostel/dashboard_tenant.html", context)


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, "hostel/rooms.html", {"rooms": rooms})


@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user) if not request.user.is_staff else Payment.objects.all()
    total_amount = sum(payment.amount for payment in payments)
    total_paid = sum(payment.paid_amount for payment in payments)
    remaining_total = sum(payment.get_remaining_amount() for payment in payments)
    context = {
        "payments": payments,
        "total_amount": total_amount,
        "total_paid": total_paid,
        "remaining_total": remaining_total,
    }
    return render(request, "hostel/payments.html", context)


@login_required
def complaint_list(request):
    if request.user.is_staff:
        complaints = Complaint.objects.all()
    else:
        complaints = Complaint.objects.filter(user=request.user)
    form = ComplaintForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        complaint = form.save(commit=False)
        complaint.user = request.user
        complaint.save()
        messages.success(request, "Complaint submitted successfully.")
        return redirect("complaints")
    return render(request, "hostel/complaints.html", {"complaints": complaints, "form": form})


@login_required
def announcement_list(request):
    announcements = Announcement.objects.filter(active=True)
    return render(request, "hostel/announcements.html", {"announcements": announcements})


@login_required
def visitor_request(request):
    if request.user.is_staff:
        visitors = Visitor.objects.all()
    else:
        visitors = Visitor.objects.filter(user=request.user)
    form = VisitorRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        visitor = form.save(commit=False)
        visitor.user = request.user
        visitor.save()
        messages.success(request, "Visitor request submitted.")
        return redirect("visitor_request")
    return render(request, "hostel/visitor_requests.html", {"visitors": visitors, "form": form})


@login_required
def feedback_view(request):
    feedbacks = Feedback.objects.filter(user=request.user) if not request.user.is_staff else Feedback.objects.all()
    form = FeedbackForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user
        feedback.save()
        messages.success(request, "Feedback submitted successfully.")
        return redirect("feedback")
    return render(request, "hostel/feedback.html", {"feedbacks": feedbacks, "form": form})


@login_required
def api_rooms(request):
    rooms = Room.objects.all().values("id", "number", "room_type", "capacity", "price", "is_available")
    return JsonResponse(list(rooms), safe=False)


@login_required
def api_announcements(request):
    announcements = Announcement.objects.filter(active=True).values("id", "title", "message", "created_at")
    return JsonResponse(list(announcements), safe=False)


@login_required
@staff_required
def approve_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    visitor.approved = True
    visitor.rejected = False
    visitor.save()
    messages.success(request, f"Visitor {visitor.visitor_name} approved.")
    return redirect("manage_visitors")


@login_required
@staff_required
def delete_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    visitor.approved = False
    visitor.rejected = True
    visitor.save()
    messages.success(request, f"Visitor {visitor.visitor_name} request rejected.")
    return redirect("manage_visitors")


@login_required
@staff_required
def allocate_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == "POST":
        username = request.POST.get("username")
        tenant = User.objects.filter(username=username, is_staff=False).first()
        if tenant:
            room.assigned_to = tenant
            room.is_available = False
            room.save()
            messages.success(request, f"Room {room.number} allocated to {tenant.username}.")
            return redirect("rooms")
        messages.error(request, "Tenant not found.")
    tenants = User.objects.filter(is_staff=False)
    return render(request, "hostel/allocate_room.html", {"room": room, "tenants": tenants})


@login_required
@staff_required
def manage_rooms(request):
    form = RoomForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Room created/updated successfully.")
        return redirect("manage_rooms")
    
    rooms = Room.objects.all().order_by("number")
    context = {"form": form, "rooms": rooms}
    return render(request, "hostel/manage_rooms.html", context)


@login_required
@staff_required
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = RoomForm(request.POST or None, instance=room)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Room updated successfully.")
        return redirect("manage_rooms")
    return render(request, "hostel/update_room.html", {"form": form, "room": room})


@login_required
@staff_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    messages.success(request, f"Room {room.number} deleted successfully.")
    return redirect("manage_rooms")


@login_required
def api_rooms(request):
    rooms = Room.objects.all().values("id", "number", "room_type", "capacity", "price", "is_available")
    return JsonResponse(list(rooms), safe=False)


@login_required
def api_announcements(request):
    announcements = Announcement.objects.filter(active=True).values("id", "title", "message", "created_at")
    return JsonResponse(list(announcements), safe=False)


@login_required
@staff_required
def manage_payments(request):
    form = PaymentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Payment record created/updated successfully.")
        return redirect("manage_payments")
    
    payments = Payment.objects.all().order_by("-due_date")
    context = {"form": form, "payments": payments}
    return render(request, "hostel/manage_payments.html", context)


@login_required
@staff_required
def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    form = PaymentForm(request.POST or None, instance=payment)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Payment updated successfully.")
        return redirect("manage_payments")
    return render(request, "hostel/update_payment.html", {"form": form, "payment": payment})


@login_required
@staff_required
def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    messages.success(request, "Payment record deleted.")
    return redirect("manage_payments")


@login_required
@staff_required
def manage_announcements(request):
    form = AnnouncementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Announcement created successfully.")
        return redirect("manage_announcements")
    
    announcements = Announcement.objects.all().order_by("-created_at")
    context = {"form": form, "announcements": announcements}
    return render(request, "hostel/manage_announcements.html", context)


@login_required
@staff_required
def update_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    form = AnnouncementForm(request.POST or None, instance=announcement)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Announcement updated successfully.")
        return redirect("manage_announcements")
    return render(request, "hostel/update_announcement.html", {"form": form, "announcement": announcement})


@login_required
@staff_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    announcement.delete()
    messages.success(request, "Announcement deleted.")
    return redirect("manage_announcements")


@login_required
@staff_required
def manage_complaints(request):
    complaints = Complaint.objects.all().order_by("-created_at")
    context = {"complaints": complaints}
    return render(request, "hostel/manage_complaints.html", context)


@login_required
@staff_required
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    form = ComplaintStatusForm(request.POST or None, instance=complaint)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Complaint status updated.")
        return redirect("manage_complaints")
    return render(request, "hostel/update_complaint_status.html", {"form": form, "complaint": complaint})


@login_required
@staff_required
def manage_visitors(request):
    visitors = Visitor.objects.all().order_by("-visit_date")
    context = {"visitors": visitors}
    return render(request, "hostel/manage_visitors.html", context)


@login_required
@staff_required
def manage_food_menu(request):
    form = FoodMenuForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Food menu item added successfully.")
        return redirect("manage_food_menu")
    
    food_items = FoodMenu.objects.all().order_by("-date", "meal_type")
    context = {"form": form, "food_items": food_items}
    return render(request, "hostel/manage_food_menu.html", context)


@login_required
@staff_required
def update_food_menu(request, food_id):
    food = get_object_or_404(FoodMenu, id=food_id)
    form = FoodMenuForm(request.POST or None, instance=food)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Food menu item updated.")
        return redirect("manage_food_menu")
    return render(request, "hostel/update_food_menu.html", {"form": form, "food": food})


@login_required
@staff_required
def delete_food_menu(request, food_id):
    food = get_object_or_404(FoodMenu, id=food_id)
    food.delete()
    messages.success(request, "Food menu item deleted.")
    return redirect("manage_food_menu")


@login_required
def view_food_menu(request):
    food_items = FoodMenu.objects.filter(is_available=True).order_by("-date", "meal_type")
    context = {"food_items": food_items}
    return render(request, "hostel/view_food_menu.html", context)


@login_required
def poll_list(request):
    polls = Poll.objects.filter(active=True).order_by("-created_at")
    voted_poll_ids = PollVote.objects.filter(user=request.user).values_list("poll_id", flat=True)
    context = {
        "polls": polls,
        "voted_poll_ids": list(voted_poll_ids),
    }
    return render(request, "hostel/poll_list.html", context)


@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, active=True)
    options = poll.options.all()
    user_vote = PollVote.objects.filter(user=request.user, poll=poll).first()
    context = {
        "poll": poll,
        "options": options,
        "user_vote": user_vote,
    }
    return render(request, "hostel/poll_detail.html", context)


@login_required
def vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, active=True)
    if request.method != "POST":
        return redirect("poll_detail", poll_id=poll.id)

    option_id = request.POST.get("option")
    option = get_object_or_404(PollOption, id=option_id, poll=poll)
    vote, created = PollVote.objects.update_or_create(
        user=request.user,
        poll=poll,
        defaults={"option": option},
    )
    messages.success(request, "Your vote has been recorded.")
    return redirect("poll_list")


@login_required
@staff_required
def manage_polls(request):
    from .forms import PollForm

    form = PollForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        poll = form.save(commit=False)
        poll.created_by = request.user
        poll.save()
        option_lines = form.cleaned_data.get("options", "").splitlines()
        for line in option_lines:
            option_text = line.strip()
            if option_text:
                PollOption.objects.create(poll=poll, option_text=option_text)
        messages.success(request, "Poll created successfully.")
        return redirect("manage_polls")

    polls = Poll.objects.all().order_by("-created_at")
    return render(request, "hostel/manage_polls.html", {"form": form, "polls": polls})


@login_required
def create_poll(request):
    from .forms import TenantPollForm

    if request.user.is_staff:
        return redirect("manage_polls")

    form = TenantPollForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        poll = form.save(commit=False)
        poll.created_by = request.user
        poll.is_admin_poll = False
        poll.save()
        option_lines = form.cleaned_data.get("options", "").splitlines()
        for line in option_lines:
            option_text = line.strip()
            if option_text:
                PollOption.objects.create(poll=poll, option_text=option_text)
        messages.success(request, "Tenant poll created successfully.")
        return redirect("poll_list")

    return render(request, "hostel/create_poll.html", {"form": form})
