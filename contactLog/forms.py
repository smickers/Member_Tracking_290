from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget, Textarea
from .models import contactLog
from django import forms

class ContactLogForm(ModelForm):
    class Meta:
        model = contactLog

        fields = '__all__'
        labels = {
            'memberID' : 'Saskpolytech ID',
            'date' : 'Date of Contact',
            'description' : 'Contact Description'
        }

        widgets = {
            'memberID' : NumberInput(attrs={'min':1,'max':999999999,}),
            'date' : SelectDateWidget(),
            'description' : forms.Textarea(attrs={'maxlength' : '150',}),
        }