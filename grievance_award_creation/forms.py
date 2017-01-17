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
        self.fields['file_field'] = FileField(widget=ClearableFileInput(attrs={'multiple': True, 'accept': FILE_EXT_TO_ACCEPT_STR} ))
        self.fields['file_description'] = CharField(widget= forms.TextInput(attrs={'type':'hidden'}))


    def save(self, commit=False):
        obj = super(ModelForm, self).save()
        for f in self.files.getlist('file_field'):
            temp = File(file=f)
            griev_file = GrievanceFiles()
            griev_file.award = obj
            griev_file.file = temp
            griev_file.save()
        #print(obj.pk)
        # print(self.__dict__)
        return obj

    def clean_file_field(self):
        # print(self.files.getlist('file_field')[0].name)
        for f in self.files.getlist('file_field'):
            print(f.size)
            if(f.size > settings.MAX_FILE_SIZE):
                raise ValidationError("File exceeds maximum size allowed")
            if(f.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT):
                raise ValidationError("File has exception which is not allowed")
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
            'recipient' : NumberInput(),
            'case' : NumberInput()
        }





class GrievanceUploadFileForm(ModelForm):
    class Meta:
        model = GrievanceFiles
        exclude = ['date_uploaded']