from django import forms
from .models import Applicant, Booking, Payment

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {
            'id_number': forms.NumberInput(attrs={'max': 9999999999}),
            'mobile_number': forms.NumberInput(attrs={'max': 999999999999999}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
