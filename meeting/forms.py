from django.forms import ModelForm, SelectDateWidget, FileField, ClearableFileInput, CharField, Textarea
from .models import Meeting, MeetingFiles
from datetime import date
from django import forms
from spfa_mt import kvp
from django.core.files import File
from .validators import *
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT, FILE_EXT_TO_ACCEPT_STR
from django import forms

# Class: MeetingForm
# Purpose: Puts together a form for creating a meeting
class MeetingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['file_field'] = FileField(required=False,
                                              widget=ClearableFileInput(
                                                  attrs={'mulitple': True, 'accept': FILE_EXT_TO_ACCEPT_STR}))
        self.fields['file_description'] = CharField(required=False, label='File Description',
                                                    widget=forms.TextInput(attrs={'type': '', 'size': '100%'}))

    def save(self, commit=False):
        # Try to save the regular member, not including the file
        try:
            obj = super(ModelForm, self).save()
        # Show the thrown error if member save throws one
        except ValidationError:
            return ValidationError
        # If a file is in the file field
        if self.files != {}:
            # Get the file from the file field
            file_to_save = self.files.getlist('file_field')[0]
            # Create an instance of the grabbed file
            tempFile = File(file = file_to_save)
            # Get the description
            desc = self.cleaned_data['file_description']
            # Create a meeting file, with the information we have grabbed from the fields
            meeting_file = MeetingFiles(fileName = tempFile, fileDesc=desc, relatedMeeting=obj)
            # Clean the file
            meeting_file.full_clean()
            # Save the file
            meeting_file.save()
        return obj

    def clean(self):
        super(MeetingForm, self).clean()
        return self.cleaned_data

    # Function: clean_file_field()
    # Purpose: Cleans the model before data is saved to the database
    # Will really only happen if there are any files to be uploaded
    def clean_file_field(self):
        if self.files != {}:
            # For each file we have; Currently only one allowed at a time
            for f in self.files.getlist('file_field'):
                # Validate the size of the file
                if f.size > MAX_FILE_SIZE:
                    raise ValidationError("File exceeds maximum size allowed")
                # Validate the file extension
                if f.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT:
                    raise ValidationError("File type is not allowed")
            # if no validation errors are thrown return the file
            return self.cleaned_data['file_field']

    class Meta:
        model = Meeting

        # Date range is +- 5 years

        # Make the range +6 on the high end, because this function doesn't
        # include the end range value
        YEARS = range(date.today().year - 5, date.today().year + 6)
        YEARS.sort()

        # Show all fields and set up labels
        fields = '__all__'
        labels = {
            'committee': 'Committee',
            'liaison': 'SPFA Liason',
            'members_attending': 'Members Attending',
            'description': 'Description',
            'date': 'Meeting Date'
        }

        # Use some special widgets for certain fields
        widgets = {
            'date': SelectDateWidget(months=kvp.MONTHS, years=YEARS),
            'description': Textarea(),
            'members_attending': forms.SelectMultiple(
                attrs={'class': 'js-members_attending'}),
            'committee': forms.Select(
                attrs={'class': 'js-committee'})
        }

