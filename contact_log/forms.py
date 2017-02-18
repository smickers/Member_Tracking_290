# SPFA MT CST Project
# November 7, 2016
from django.forms import ModelForm, SelectDateWidget, FileField, ClearableFileInput, CharField
from .models import contactLog, ContactLogFile
from django import forms
from django.forms import Textarea
from datetime import datetime
from spfa_mt import kvp, settings
from django.core.exceptions import ValidationError
from django.core.files import File


# Purpose: This class is used to build up a form, that
# can be used to enter a new contact log
class ContactLogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['file_field'] = FileField(required=False,
                                              widget=ClearableFileInput(
                                                  attrs={'multiple': False, 'accept': kvp.CONTACT_LOG_FILE_EXTENSIONS}))
        self.fields['file_description'] = CharField(required=False, label='File Description',
                                                    widget=forms.TextInput(attrs={'type': '', 'size': '100%'}))

    def save(self, commit=False):
        """
        Function: save
        Purpose: When the contact log is saved this method will be called to do some file validation
        :param commit:
        :return: obj - Model Form
        """
        try:
            obj = super(ModelForm, self).save()
        except ValidationError:
            return ValidationError

        # Files do not have to be uploaded, but if they are, save the file
        if self.files != {}:
            f = self.files.getlist('file_field')[0]
            temp = File(file=f)
            desc = self.cleaned_data['file_description']
            cl_file = ContactLogFile(relatedContactLog=obj, fileName=temp, description=desc)
            cl_file.save()

        return obj

    def clean_file_field(self):
        """
        Function: clean
        Purpose: Cleans the models before they are entered into the database
        :return:
        """
        # Clean uploaded files if there are any
        if self.files != {}:
            for f in self.files.getlist('file_field'):
                print f.size
                if f.size > settings.MAX_FILE_SIZE:
                    raise ValidationError("File exceeds maximum size allowed")
                if f.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
                    raise ValidationError("File type is not allowed")
            return self.cleaned_data['file_field']

    class Meta:
        model = contactLog
        # Specifying the fields to be shown in the form
        fields = [
            'member',
            'description',
            'contactCode',
            'date'
        ]
        # Giving labels to fields defined above
        labels = {
            'member': 'Saskpolytech Member',
            'description': 'Contact Description',
            'contactCode': 'Contact Code',
            'date': 'Date of Contact'
        }
        # Defining a number input for the memberID
        widgets = {
            'member': forms.Select(
                attrs={'class': 'js-member', 'id': 'member_select'}),
            'date': SelectDateWidget(months=kvp.MONTHS, years=range(datetime.now().year - 5, datetime.now().year + 6)),
            'description': Textarea(attrs={'rows': '2'})
        }
