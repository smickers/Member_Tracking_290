from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget, Textarea
from .models import contactLog
import datetime
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
            'memberID' : NumberInput(attrs={'min':1,'max':999999999}),
            'date' : SelectDateWidget(years=range(1959, datetime.datetime.now().year + 1),),
            #'description': forms.CharField(attrs={'maxlength': '150', }),
            #'description' : forms.CharField(attrs={'maxlength' : '150',}),
        }