from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Person
from .validators import *
import re
import datetime


#The form used for modifying/adding a member
class PersonForm(ModelForm):
    class Meta:

        model = Person

        #specifies which field are going to be used on the form
        fields = '__all__'

        #specifies labels for all the fields found in the model
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

        # Set up a custom error message for postal codes that are too long
        # This is used to override the default max_length message.
        error_messages = {
            'pCode': {
                'max_length': "Postal code entered is too long. Must be in the form A#A #A#.",
            },
        }

        #modifies the date fields to have a valid range
        widgets = {
            'bDay': SelectDateWidget(years=range(1900, datetime.datetime.now().year + 1)),
            'hireDate': SelectDateWidget(years=range(1900, datetime.datetime.now().year + 1))
            }




