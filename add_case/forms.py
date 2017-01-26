from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Case
from django import  forms
from datetime import date
from django.forms import ModelForm, SelectDateWidget
from .models import *
from django import forms
from .fields import ListTextWidget
import re


# Creating the Form data for Cases ...
class CaseForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['satellite'].widget = ListTextWidget(data_list=list(CaseSatellite.objects.all()),
                                                         name='satellite-list')

    class Meta:
        model = Case
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
             'date': SelectDateWidget(months=MONTHS, years=YEARS),
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
