from django import forms
from .models import TestSlot
from .models import TestCenter

class TestSlotForm(forms.ModelForm):
    class Meta:
        model = TestSlot
        fields = ['center', 'date', 'time', 'max_applicants']

class TestCenterForm(forms.ModelForm):
    class Meta:
        model = TestCenter
        fields = ['name', 'location', 'capacity']