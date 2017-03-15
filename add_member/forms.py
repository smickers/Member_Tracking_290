from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Person
from .validators import *
import re
import datetime
from django import forms
import django
#The form used for modifying/adding a member
class PersonForm(ModelForm):
    class Meta:
        MONTHS = {
            1: 'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sep',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec'
        }

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
            'bDay': SelectDateWidget(months=MONTHS, years=range(1900, datetime.datetime.now().year + 1)),
            'hireDate': SelectDateWidget(months=MONTHS, years=range(1900, datetime.datetime.now().year + 1))
            }


class MemberFilterForm(forms.Form):
    """
    This is the form that is used to filter members. We're only using this to generate the fields and labels.
    The form itself is not submitted. The page will do javascript to get the values from the inputs and do an ajax request.
    """
    JOB_TYPE = Person.POSITION_CLASS_CHOICE
    JOB_TYPE.insert(0, ('', '-----'))
    # All of the fields we are filtering with.
    memberID = forms.IntegerField(label='Member ID', widget=forms.NumberInput(attrs={'placeholder': 'Member ID'}), required=False)
    firstName = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=False)
    middleName = forms.CharField(label='Middle Name', widget=forms.TextInput(attrs={'placeholder': 'Middle Name'}), required=False)
    lastName = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=False)
    min_bDay = forms.DateField(label='Minimum Birth Date', widget=PersonForm.Meta.widgets['bDay'],required=False)
    max_bDay = forms.DateField(label='Maximum Birth Date', widget=PersonForm.Meta.widgets['bDay'], required=False)
    gender = forms.ChoiceField(choices=Person.GENDER_CHOICE, required=False)
    socNum = forms.IntegerField(label='SIN', widget=forms.NumberInput(attrs={'placeholder': 'Social Insurance Number'}), required=False)
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder': 'City'}), required=False)
    mailAddress = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address'}), required=False)
    mailAddress2 = forms.CharField(label='Address #2', widget=forms.TextInput(attrs={'placeholder': 'Address #2'}), required=False)
    pCode = forms.CharField(max_length=7, label='Postal Code', widget=forms.TextInput(attrs={'placeholder': 'A1A 1A1'}), required=False)
    hPhone = forms.CharField(label='Home Phone', widget=forms.TextInput(attrs={'placeholder': '(123)123-4567'}), required=False)
    cPhone = forms.CharField(label='Cell Phone', widget=forms.TextInput(attrs={'placeholder': '(123)123-4567'}), required=False)
    hEmail = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'placeholder': 'someone@email.com'}), required=False)
    campus = forms.CharField(label='Campus', widget=forms.TextInput(attrs={'placeholder': 'Sask Polytech Campus'}), required=False)
    jobType = forms.ChoiceField(label='Job Type', choices=Person.POSITION_CLASS_CHOICE, required=False)
    committee = forms.CharField(label='Committee', widget=forms.TextInput(attrs={'placeholder': 'Committee'}), required=False)
    membershipStatus = forms.CharField(label='Membership Status', widget=forms.TextInput(attrs={'placeholder': 'Membership Status'}), required=False)
    min_hDay = forms.DateField(label='Minimum Hire Date', widget=PersonForm.Meta.widgets['hireDate'], required=False)
    max_hDay = forms.DateField(label='Maximum Hire Date', widget=PersonForm.Meta.widgets['hireDate'], required=False)
