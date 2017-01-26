from django.forms import ModelForm, SelectDateWidget, Textarea, RadioSelect, NumberInput, FileField, ClearableFileInput, CharField
from .models import GrievanceAward, GrievanceFiles
from datetime import date
from spfa_mt.settings import FILE_EXT_TO_ACCEPT_STR
from django.http import HttpResponseRedirect
from spfa_mt import settings
from django.core.exceptions import ValidationError
from django.core.files import File
from django import forms



# Class: GrievanceAwardForm
# Purpose: Puts together a form for creating a grievance award
class GrievanceAwardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['file_field'] = FileField(required=False,widget=ClearableFileInput(attrs={'multiple': False, 'accept': FILE_EXT_TO_ACCEPT_STR} ))
        self.fields['file_description'] = CharField(required=False, label='File Description', widget= forms.TextInput(attrs={'type':'', 'size':'100%'}))




    def save(self, commit=False):
        """
        Function: save
        Purpose: When grievance award is saved this method will be called to do some extra validation
        :param commit:
        :return: obj - Model Form
        """
        try:
            obj = super(ModelForm, self).save()
        except ValidationError:
            return ValidationError

        #Files do not have to be uploaded, but if they are, save the file
        if self.files != {}:
            f = self.files.getlist('file_field')[0]
            temp = File(file=f)
            desc = self.cleaned_data['file_description']
            griev_file = GrievanceFiles(award=obj, file=temp,
                                        description=desc)
            griev_file.save()

        return obj

    def clean_file_field(self):
        """
        Function: clean
        Purpose: Cleans the models before they are entered into the database
        :return:
        """
        # print(self.files not None)
        #print(self.files != {})

        #Clean uploaded files if there are any
        if self.files != {}:
            # print(self.files.getlist('file_field')[0].name)
            for f in self.files.getlist('file_field'):
                print(f.size)
                if(f.size > settings.MAX_FILE_SIZE):
                    raise ValidationError("File exceeds maximum size allowed")
                if(f.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT):
                    raise ValidationError("File type is not allowed")
            return self.cleaned_data['file_field']



    # Class: Meta
    # Purpose: Builds up a new form for creating a GA
    class Meta:
        model = GrievanceAward

        # Date range is +- 5 years

        # Make the range +6 on the high end, because this function doesn't
        # include the end range value
        YEARS = range(date.today().year - 5, date.today().year + 6)
        YEARS.sort()

        # Define months so they're entered as three letters
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

        # Show all fields and set up labels
        fields = '__all__'
        labels = {
            'grievanceType': 'Grievance Type',
            'recipient': 'Related Recipient',
            'case': 'Related Case',
            'awardAmount': 'Award Amount',
            'description' : 'Description',
            'date' : 'Date Awarded'
        }

        # Use some special widgets for certain fields
        widgets = {
            'date': SelectDateWidget(months=MONTHS, years=YEARS),
            'description' : Textarea(),
            'grievanceType' : RadioSelect(),
            'recipient' : forms.Select(
                attrs={'class': 'js-recipient'}),
            'case' : forms.Select(
                attrs={'class': 'js-case'}),
        }


