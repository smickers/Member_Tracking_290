from django.forms import ModelForm, NumberInput, SelectDateWidget
from .models import contactLog
from django import forms
from datetime import date, datetime

class ContactLogForm(ModelForm):
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1959, datetime.now().year + 1)), initial=datetime.now)
    class Meta:
        model = contactLog

        #fields = '__all__'
        fields = [
            'memberID',
            'date',
            'description',
        ]
        labels = {
            'memberID' : 'Saskpolytech ID',
            'date' : 'Date of Contact',
            'description' : 'Contact Description'
        }

        widgets = {
            'memberID' : NumberInput(attrs={'min':1,'max':999999999}),
            #'date' : SelectDateWidget(years=range(1959, datetime.datetime.now().year + 1),),
            #'description': forms.CharField(attrs={'maxlength': '150', }),
            #'description' : forms.CharField(attrs={'maxlength' : '150',}),
        }