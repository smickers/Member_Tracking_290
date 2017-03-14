from django.forms import ModelForm, SelectDateWidget, FileField, ClearableFileInput, CharField
from .models import Person, MemberFiles
from django import forms
from spfa_mt import kvp
from django.core.files import File
from .validators import *
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT, FILE_EXT_TO_ACCEPT_STR
import datetime


# The form used for modifying/adding a member
class PersonForm(ModelForm):
    # Overloading the init method, to add file field/desc separately from the rest of the form.
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['file_field'] = FileField(required=False,
                                              widget=ClearableFileInput(
                                                  attrs={'multiple': True, 'accept': FILE_EXT_TO_ACCEPT_STR}))
        self.fields['file_description'] = CharField(required=False, label='File Description',
                                                    widget=forms.TextInput(attrs={'type': '', 'size': '100%'}))

    # FUNCTION: save()
    # PURPOSE:  Overload the save() method to ensure member can be saved,
    # # and then save the file, associating it with the member
    def save(self, commit=False):
        # Try to save the regular member, excluding the file
        try:
            obj = super(ModelForm, self).save()
        # If saving the member throws an error, show the error
        except ValidationError:
            return ValidationError
        # If a file exists to save
        if self.files != {}:
            # Get the save file
            save_file = self.files.getlist('file_field')[0]
            # Create an file instance of the file we just got
            temp = File(file=save_file)
            # Indicate what the description should be
            desc = self.cleaned_data['file_description']
            # Create a member file, with information from the file fields and the member object
            mem_file = MemberFiles(fileName=temp, fileDesc=desc, relatedMember=obj)
            # Clean it again, Sam.
            mem_file.full_clean()
            mem_file.save()
        return obj

    def clean(self):
        super(PersonForm, self).clean()
        return self.cleaned_data

    # FUNCTION:     clean_file_field()
    # PURPOSE:      Cleans the models before they are entered into the database
    def clean_file_field(self):
        # if there are any files,
        if self.files != {}:
            # For each file we got (we only got one, simultaneous uploads currently not supported)
            for f in self.files.getlist('file_field'):
                # validate file size
                if f.size > MAX_FILE_SIZE:
                    raise ValidationError("File exceeds maximum size allowed")
                # validate file extention
                if f.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT:
                    raise ValidationError("File type is not allowed")
            # if everything is cool, return the cleaned file
            return self.cleaned_data['file_field']

    class Meta:
        model = Person
        # specifies which field are going to be used on the form
        fields = '__all__'

        # specifies labels for all the fields found in the model
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

        # modifies the date fields to have a valid range
        widgets = {
            'bDay': SelectDateWidget(months=kvp.MONTHS, years=range(1900, datetime.datetime.now().year + 1)),
            'hireDate': SelectDateWidget(months=kvp.MONTHS, years=range(1900, datetime.datetime.now().year + 1))
            }




