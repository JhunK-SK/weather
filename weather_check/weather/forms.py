from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter a city',
                'class': "form-control",
            }),
        }