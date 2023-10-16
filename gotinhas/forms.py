from django import forms
from .models import Gotinhas

class GotinhasForm(forms.ModelForm):
    class Meta:
        model = Gotinhas
        fields = ['first_name', 'last_name', 'birthdate']
