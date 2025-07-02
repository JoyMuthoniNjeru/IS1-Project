from django.db import models

class Booking(models.Model):
    driving_school = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100)
    pdl_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    license_type = models.CharField(max_length=50)
    test_date = models.DateField()
    time_slot = models.CharField(max_length=30)
    document = models.FileField(upload_to='uploads/')


    def __str__(self):
        return f"{self.name} - {self.id_number}"
