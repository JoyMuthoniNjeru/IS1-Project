from django.db import models
from booking.models import Booking  

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('mpesa', 'Mpesa'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)  
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pin = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.name} - {self.amount}"

