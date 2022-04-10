from django import forms
from datetime import date
from django.forms import ModelForm
from eLibrary.settings import DATE_INPUT_FORMATS
from .models import Author


class AuthorForm(ModelForm):
    """forma bazująca na modeli Author przez class Meta"""
    # date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Data urodzenia')

    class Meta:
        model = Author
        fields = ['name', 'nationality', 'date_of_birth', 'date_of_death']



