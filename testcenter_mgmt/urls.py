from django.urls import path
from . import views

app_name = 'testcenter_mgmt'

urlpatterns = [
    path('test-centers/', views.test_center_dashboard, name='test_center_dashboard'),
    path('test-centers/add/', views.add_test_center, name='add_test_center'),
    path('test-centers/edit/<int:pk>/', views.edit_test_center, name='edit_test_center'),
    path('test-centers/delete/<int:pk>/', views.delete_test_center, name='delete_test_center'),
]
