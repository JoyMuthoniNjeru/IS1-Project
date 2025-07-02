from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-slot-config/', views.slot_configuration, name='adminslotconfig')
]