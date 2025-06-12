from django.contrib import admin
from .models import Applicant, Booking, Payment

admin.site.register(Applicant)
admin.site.register(Booking)
admin.site.register(Payment)

