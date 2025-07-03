from django import forms
from .models import TestCenter

class TestCenterForm(forms.ModelForm):
    class Meta:
        model = TestCenter
        fields = ['name', 'location', 'capacity']
