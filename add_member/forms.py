from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['memberID', 'firstName', 'middleName', 'socNum',
                  'city', 'mailAddress', 'mailAddress2', 'pCode',
                  'bDay', 'gender', 'hPhone', 'cPhone', 'hEmail',
                  'campus', 'jobType', 'committee', 'memberImage']
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
        error_messages = {
            'name':
                {
                    'max_length': 'Member ID should be less than 9 digits',
                },
        }

