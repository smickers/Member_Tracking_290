from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import *
from django import forms
from .fields import ListTextWidget
import re


class CaseForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['satellite'].widget = ListTextWidget(data_list=list(CaseSatellite.objects.all()), name='satellite-list')

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
            'additionalMembers': 'Additional SPFA members',
            'additionalNonMembers': 'Additional non-members',
            'docs': 'Related documents',
            'logs': 'Logs',
            'date': 'Date',
        }

        widgets = {
            'date': SelectDateWidget(),
            'complainant': forms.Select(
                attrs={'class': 'js-complainant'}),
            'additionalMembers': forms.SelectMultiple(
                attrs={'class': 'js-additional_members'})
        }

