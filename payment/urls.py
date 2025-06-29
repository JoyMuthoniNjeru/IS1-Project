from django.urls import path
from .views import payment_form, payment_success

app_name = 'payment'

urlpatterns = [
    path('', payment_form, name='payment_form'), 
    path('success/', payment_success, name='payment_success'), 
]

