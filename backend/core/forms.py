from django import forms
from .models import TestSlot
from .models import TestCenter

class TestSlotForm(forms.ModelForm):
    class Meta:
        model = TestSlot
        fields = ['center', 'date', 'time', 'max_applicants']

    def __init__(self, *args, **kwargs):
        manager_centers = kwargs.pop('manager_centers', None)
        super().__init__(*args, **kwargs)
        if manager_centers is not None:
            self.fields['center'].queryset = manager_centers

class TestCenterForm(forms.ModelForm):
    class Meta:
        model = TestCenter
        fields = ['name', 'location', 'capacity']