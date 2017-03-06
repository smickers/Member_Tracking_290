from datetime import date
from django.forms import ModelForm, SelectDateWidget, ModelMultipleChoiceField, FileField, ClearableFileInput, CharField
from .models import *
from django import forms
from .fields import ListTextWidget
from spfa_mt import kvp
from spfa_mt.settings import FILE_EXT_TO_ACCEPT_STR
from django.core.files import File


# Creating the Form data for Cases ...
class CaseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['satellite'].widget = ListTextWidget(data_list=list(CaseSatellite.objects.all()),
                                                         name='satellite-list')

        self.fields['file_field'] = FileField(required=False, widget=ClearableFileInput(
            attrs={'multiple': False, 'accept': FILE_EXT_TO_ACCEPT_STR}))
        self.fields['file_description'] = CharField(required=False, label='File Description',
                                                    widget=forms.TextInput(attrs={'type': '', 'size': '100%'}))

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
            case_file = CaseFiles(case=obj, file=temp,
                                        description=desc)
            case_file.save()

        return obj

    def clean_additionalMembers(self):
        pass

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
                #print(f.size)
                if(f.size > MAX_FILE_SIZE):
                    raise ValidationError("File exceeds maximum size allowed")
                if(f.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT):
                    raise ValidationError("File type is not allowed")
            return self.cleaned_data['file_field']

    class Meta:
        model = Case
        # Date range is +- 5 years

        # Make the range +6 on the high end, because this function doesn't
        # include the end range value
        YEARS = range(date.today().year - 5, date.today().year + 6)
        YEARS.sort()

        fields = '__all__'
        labels = {
            'lead': 'Lead',
            'complainant': 'Complainant',
            'campus': 'Campus',
            'caseType': 'Case Type',
            'satellite': 'Satellite',
            'program': 'Program',
            'status': 'Status',
            'additionalMembers': 'Additional SPFA Members',
            'additionalNonMembers': 'Additional Non-Members',
            'docs': 'Related Documents',
            'logs': 'Logs',
            'date': 'Date',
        }

        widgets = {
             'date': SelectDateWidget(months=kvp.MONTHS, years=YEARS),
             'complainant': forms.Select(
                attrs={'class': 'js-complainant', 'style': 'width:65%;'}),
             'additionalMembers': forms.SelectMultiple(
                attrs={'class': 'js-additional_members', 'style': 'width:65%'}),
             'program': forms.Select(
                attrs={'style': 'width:50%;'}
             )
        }

        error_messages = {
            'complainant': {
                'invalid': "Complainant cannot be added as an additional member.",
                'invalid_choice': "Complainant cannot be added as an additional member."
            },
            'additionalMembers': {
                'invalid': "Complainant cannot be added as an additional member.",
                'invalid_choice': "Complainant cannot be added as an additional member."
            }
        }


class CaseMembersForm(ModelForm):
    class Meta:
        model = Case
        fields = ('additionalMembers', 'additionalNonMembers')

    # field from which you will pick additional members to add to the case, after the case has
    # been created.
    additionalMembers = ModelMultipleChoiceField(queryset=(), to_field_name="pk", label='Members', required=False)

    # constructor method.
    def __init__(self, **kwargs):
        super(CaseMembersForm, self).__init__(**kwargs)
        self.fields['additionalMembers'].queryset = Person.objects.exclude(case=self.instance)

    # combines the initial and the new set of additional members
    def clean_additional_members(self):
        cleaned_data = super(CaseMembersForm, self).clean()
        cn = cleaned_data.get('complainant')
        additional_members = cleaned_data.get('additionalMembers')
        print(additional_members)

        for mem in additional_members:
            # cn cannot be an additional member
            if mem and cn and mem is cn:
                msg = "Complainant cannot be added as an additional member."
                self.add_error("additionalMembers", msg)
                # raise ValidationError("Complainant cannot be added as an additional member.")
        return self.initial['additionalMembers'] | self.cleaned_data['additionalMembers']
