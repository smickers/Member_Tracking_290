# SPFA MT CST Project
# November 7, 2016
from django.forms import ModelForm, NumberInput
from .models import contactLog
from django import forms
from datetime import datetime

# Purpose: This class is used to build up a form, that
# can be used to enter a new contact log
class ContactLogForm(ModelForm):

    # Defining the date field up here, because we were
    # getting errors with it in the widgets section
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1959,
                       datetime.now().year + 1)), initial=datetime.now)
    class Meta:
        model = contactLog

        # Specifying the fields to be shown in the form
        fields = [
            'memberID',
            'date',
            'description',
        ]

        # Giving labels to fields defined above
        labels = {
            'memberID' : 'Saskpolytech ID',
            'date' : 'Date of Contact',
            'description' : 'Contact Description'
        }

        # Defining a number input for the memberID
        widgets = {
            'memberID' : NumberInput(attrs={'min':1,'max':999999999}),
        }

