from django.db import models

class Booking(models.Model):
    driving_school = models.CharField(max_length=100, default="N/A")
    id_number = models.CharField(max_length=10, default="0000000000")
    name = models.CharField(max_length=100, default="Unknown")
    pdl_number = models.CharField(max_length=20, default="N/A")
    gender = models.CharField(max_length=10, default="Not specified")
    date_of_birth = models.DateField(default="2000-01-01")  # or use timezone.now if appropriate
    nationality = models.CharField(max_length=50, default="Unknown")
    country = models.CharField(max_length=100, default="Unknown")
    mobile = models.CharField(max_length=15, default="0000000000")
    email = models.EmailField(default="user@example.com")
    license_type = models.CharField(max_length=50, default="B")
    test_date = models.DateField(default="2025-07-01")
    time_slot = models.CharField(max_length=30, default="09:00 AM")
    document = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id_number}"



