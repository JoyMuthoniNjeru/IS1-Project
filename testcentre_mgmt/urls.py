from django.urls import path
from . import views

app_name = 'testcentre_mgmt'

urlpatterns = [
    path('test-centres/', views.test_centre_dashboard, name='test_centre_dashboard'),
    path('test-centres/add/', views.add_test_center, name='add_test_centre'),
    path('test-centres/edit/<int:pk>/', views.edit_test_centre, name='edit_test_centre'),
    path('test-centres/delete/<int:pk>/', views.delete_test_centre, name='delete_test_centre'),
]
