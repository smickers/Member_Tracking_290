from django.forms import ModelForm, SelectDateWidget, FileField, ClearableFileInput, CharField
from .models import Person, MemberFiles
from django import forms
from spfa_mt import kvp
from django.core.files import File
from .validators import *
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT, FILE_EXT_TO_ACCEPT_STR
import datetime
from django import forms
import django
#The form used for modifying/adding a member
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
            'city': 'City',
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


class MemberFilterForm(forms.Form):
    """
    This is the form that is used to filter members. We're only using this to generate the fields and labels.
    The form itself is not submitted. The page will do javascript to get the values from the inputs and do an ajax request.
    """
    # JOB_TYPE = Person.POSITION_CLASS_CHOICE
    # JOB_TYPE.insert(0, ('', '-----'))
    # All of the fields we are filtering with.
    memberID = forms.IntegerField(label='Member ID', widget=forms.NumberInput(attrs={'placeholder': 'Member ID'}), required=False)
    firstName = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=False)
    middleName = forms.CharField(label='Middle Name', widget=forms.TextInput(attrs={'placeholder': 'Middle Name'}), required=False)
    lastName = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=False)
    min_bDay = forms.DateField(label='Birth Date From:', widget=PersonForm.Meta.widgets['bDay'],required=False)
    max_bDay = forms.DateField(label='Birth Date To:', widget=PersonForm.Meta.widgets['bDay'], required=False)
    gender = forms.ChoiceField(choices=kvp.GENDER_CHOICE, required=False)
    socNum = forms.IntegerField(label='SIN', widget=forms.NumberInput(attrs={'placeholder': 'Social Insurance Number'}), required=False)
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder': 'City'}), required=False)
    mailAddress = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address'}), required=False)
    mailAddress2 = forms.CharField(label='Address #2', widget=forms.TextInput(attrs={'placeholder': 'Address #2'}), required=False)
    pCode = forms.CharField(max_length=7, label='Postal Code', widget=forms.TextInput(attrs={'placeholder': 'A1A 1A1'}), required=False)
    hPhone = forms.CharField(label='Home Phone', widget=forms.TextInput(attrs={'placeholder': '(123)123-4567'}), required=False)
    cPhone = forms.CharField(label='Cell Phone', widget=forms.TextInput(attrs={'placeholder': '(123)123-4567'}), required=False)
    hEmail = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'placeholder': 'someone@email.com'}), required=False)
    campus = forms.ChoiceField(label='Campus', choices=kvp.CAMPUS_CHOICE, required=False)
    jobType = forms.ChoiceField(label='Job Type', choices=kvp.POSITION_CLASS_CHOICE, required=False)
    committee = forms.CharField(label='Committee', widget=forms.TextInput(attrs={'placeholder': 'Committee'}), required=False)
    membershipStatus = forms.ChoiceField(label='Membership Status', choices=kvp.MEMBERSHIP_STATUS, required=False)
    min_hDay = forms.DateField(label='Hire Date From:', widget=PersonForm.Meta.widgets['hireDate'], required=False)
    max_hDay = forms.DateField(label='Hire Date To:', widget=PersonForm.Meta.widgets['hireDate'], required=False)
    programChoice = forms.CharField(label='Program', widget=forms.TextInput(attrs={'placeholder': 'Program'}), required=False)
