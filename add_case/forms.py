from django.forms import ModelForm, SelectDateWidget
from .models import *
from django import forms
from .fields import ListTextWidget


# Creating the Form data for Cases ...
class CaseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['satellite'].widget = ListTextWidget(data_list=list(CaseSatellite.objects.all()),
                                                         name='satellite-list')

    class Meta:
        model = Case

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
            'date': SelectDateWidget(),
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