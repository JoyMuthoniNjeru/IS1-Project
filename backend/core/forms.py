from django import forms
from .models import TestSlot

class TestSlotForm(forms.ModelForm):
    class Meta:
        model = TestSlot
        fields = ['date', 'time', 'location', 'max_applicants']