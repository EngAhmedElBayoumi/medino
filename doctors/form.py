from dataclasses import field, fields
from django import forms
from .models import doctor


class doctor_form(forms.ModelForm):
    class Meta:
        model = doctor
        fields='__all__'
       