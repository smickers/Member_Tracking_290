from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Person
from .validators import *
import re

class PersonForm(ModelForm):
    class Meta:
        model = Person

        fields = '__all__'
        labels = {
            'memberID': 'Member ID/Saskpoly ID',
            'firstName': 'First Name',
            'middleName': 'Middle Name',
            'socNum': 'SIN',
            'city':'City',
            'mailAddress': 'Mail Address',
            'mailAddress2': 'Mail Address 2',
            'pCode':'Postal Code',
            'bDay':'Birth Date',
            'gender': 'Gender',
            'hPhone': 'Home Phone',
            'cPhone': 'Cell Phone',
            'hEmail': 'Home Email',
            'campus': 'Campus',
            'jobType': 'Job Type',
            'committee': 'Committee',
            'memberImage': 'Member Image',
            }

        widgets = {
            'memberID': NumberInput(attrs={'min':0,'max':999999999}),
            'socNum': NumberInput(attrs={'min': 0, 'max': 999999999}),
            'bDay': SelectDateWidget()
            }

    def clean_memberID(self):
        data = self.cleaned_data['memberID']
        if(data <= 99999999):
            raise ValidationError("Invalid member id")
        return data

    def clean_socNum(self):
        data = self.cleaned_data['socNum']
        if( data <= 99999999 ):
            raise  ValidationError("Invalid SIN number")
        return data

    def clean_pCode(self):
        data = self.cleaned_data['pCode']
        data = validate_pCode(data)
        return data






