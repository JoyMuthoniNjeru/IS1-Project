from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('logout/', views.logout_view, name='logout'),
    # We'll add more views here later
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('applicant/', views.applicant_dashboard, name='applicant_dashboard'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
]