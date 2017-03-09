from django.forms import ModelForm, ValidationError, SelectDateWidget, FileField, ClearableFileInput, CharField
from .models import Person, MemberFiles
from django import forms
from spfa_mt import kvp
from django.core.files import File
from .validators import *
import re
import datetime


# The form used for modifying/adding a member
class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['file_field'] = FileField(required=False,
                                              widget=ClearableFileInput(
                                                  attrs={'multiple': False, 'accept': settings.FILE_EXT_TO_ACCEPT}))
        self.fields['file_description'] = CharField(required=False, label='File Description',
                                                    widget=forms.TextInput(attrs={'type': '', 'size': '100%'}))

    # Ensure member can be saved and then save the file, associating it with the member
    def save(self, commit=False):
        # Try to save the regular member, excluding the file
        try:
            obj = super(ModelForm, self).save()
        # If saving the mmebr throws an error show the error
        except ValidationError:
            return ValidationError

        # If a file exists to save
        if self.files != {}:
            # Get the save file
            save_file = self.files.getList('file_field')[0]
            temp = File(file=save_file)
            desc = self.cleaned_data['file_description']
            # Create a member file, with information from the file fields and the member object
            mem_file = MemberFiles(fileName=temp, fileDesc=desc, relatedMember=obj)
            mem_file.save()

        return obj

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
            'bDay': SelectDateWidget(months=kvp.MONTHS, years=range(1900, datetime.datetime.now().year + 1)),
            'hireDate': SelectDateWidget(months=kvp.MONTHS, years=range(1900, datetime.datetime.now().year + 1))
            }




