from django import forms
from .models import Car, Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "last_name",
            "first_name",
            "birth_date"
        ]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'