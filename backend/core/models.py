from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Represents a driving test center
class TestCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Represents a driving test slot
class TestSlot(models.Model):
    center = models.ForeignKey(TestCenter, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    max_applicants = models.PositiveIntegerField()
    current_load = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.date} at {self.time} - {self.center.name}"

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
        ('closed', 'Closed')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"{self.center.name} - {self.date} {self.time}"

# Represents a booking made by a user
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(TestSlot, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.slot}"
    
class UserProfile(models.Model):
    USER_ROLES = [
        ('applicant', 'Applicant'),
        ('admin', 'Administrator'),
        ('manager', 'Test Centre Manager'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

# Automatically create or update a UserProfile when a User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()