from django.contrib import admin
from .models import TestCenter, TestSlot, Booking, UserProfile

admin.site.register(TestCenter)
admin.site.register(TestSlot)
admin.site.register(Booking)
admin.site.register(UserProfile)
