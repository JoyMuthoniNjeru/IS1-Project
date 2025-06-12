from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    pdl_number = models.CharField(max_length=20)  # Provisional Driving License

    def __str__(self):
        return self.name


class Booking(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    test_date = models.DateField()
    test_centre = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending")  # Approved / Rejected

    def __str__(self):
        return f"{self.applicant.name} - {self.test_date}"


class Payment(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # e.g. "M-Pesa"
    payment_status = models.CharField(max_length=20, default="Pending")  # Paid / Failed

    def __str__(self):
        return f"{self.applicant.name} - {self.amount}"

