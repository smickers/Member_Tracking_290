from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Person
from .validators import *
import re
import datetime

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
            'bDay': SelectDateWidget(years=range(1980, datetime.datetime.now().year + 1)),
            'hireDate': SelectDateWidget(years=range(1980, datetime.datetime.now().year + 1))
            }




