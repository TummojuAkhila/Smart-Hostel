from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("tenant-dashboard/", views.tenant_dashboard, name="tenant_dashboard"),
    path("rooms/", views.room_list, name="rooms"),
    path("payments/", views.payment_list, name="payments"),
    path("complaints/", views.complaint_list, name="complaints"),
    path("announcements/", views.announcement_list, name="announcements"),
    path("visitor-request/", views.visitor_request, name="visitor_request"),
    path("feedback/", views.feedback_view, name="feedback"),
    path("approve-visitor/<int:visitor_id>/", views.approve_visitor, name="approve_visitor"),
    path("allocate-room/<int:room_id>/", views.allocate_room, name="allocate_room"),
    path("manage-rooms/", views.manage_rooms, name="manage_rooms"),
    path("update-room/<int:room_id>/", views.update_room, name="update_room"),
    path("delete-room/<int:room_id>/", views.delete_room, name="delete_room"),
    
    # Admin Management URLs
    path("manage-payments/", views.manage_payments, name="manage_payments"),
    path("update-payment/<int:payment_id>/", views.update_payment, name="update_payment"),
    path("delete-payment/<int:payment_id>/", views.delete_payment, name="delete_payment"),
    path("manage-announcements/", views.manage_announcements, name="manage_announcements"),
    path("update-announcement/<int:announcement_id>/", views.update_announcement, name="update_announcement"),
    path("delete-announcement/<int:announcement_id>/", views.delete_announcement, name="delete_announcement"),
    path("manage-complaints/", views.manage_complaints, name="manage_complaints"),
    path("update-complaint/<int:complaint_id>/", views.update_complaint_status, name="update_complaint"),
    path("manage-visitors/", views.manage_visitors, name="manage_visitors"),
    path("delete-visitor/<int:visitor_id>/", views.delete_visitor, name="delete_visitor"),
    path("manage-food-menu/", views.manage_food_menu, name="manage_food_menu"),
    path("update-food-menu/<int:food_id>/", views.update_food_menu, name="update_food_menu"),
    path("delete-food-menu/<int:food_id>/", views.delete_food_menu, name="delete_food_menu"),
    path("view-food-menu/", views.view_food_menu, name="view_food_menu"),
    path("polls/", views.poll_list, name="poll_list"),
    path("polls/<int:poll_id>/", views.poll_detail, name="poll_detail"),
    path("polls/<int:poll_id>/vote/", views.vote_poll, name="vote_poll"),
    path("polls/create/", views.create_poll, name="create_poll"),
    path("manage-polls/", views.manage_polls, name="manage_polls"),
    
    # API URLs
    path("api/rooms/", views.api_rooms, name="api_rooms"),
    path("api/announcements/", views.api_announcements, name="api_announcements"),
]
