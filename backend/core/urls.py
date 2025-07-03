from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/configure-slots/', views.slot_configuration, name='slot_configuration'),
    path('admin-dashboard/add-slot/', views.add_slot, name='add_slot'),
    path('admin-dashboard/configure-slots/<int:pk>/edit/', views.edit_slot, name='edit_slot'),
    path('admin-dashboard/configure-slots/<int:pk>/delete/', views.delete_slot, name='delete_slot'),
]