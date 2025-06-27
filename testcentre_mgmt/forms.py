from django import forms
from .models import TestCentre

class TestCentreForm(forms.ModelForm):
    class Meta:
        model = TestCentre
        fields = ['name', 'location', 'capacity']
