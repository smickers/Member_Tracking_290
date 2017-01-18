from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Case
from django import  forms
from datetime import date

class CaseForm(ModelForm):
    class Meta:
        model = Case

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
            'complainant': 'Complaintant',
            'campus': 'Campus',
            'caseType': 'Case Type',
            'status': 'Status',
            'additionalMembers': 'Additional SPFA members',
            'additionalNonMembers': 'Additional non-members',
            'docs': 'Related documents',
            'logs': 'Logs',
            'date': 'Date',
        }

        widgets = {
            'date': SelectDateWidget(months=MONTHS, years=YEARS),
            'complainant': forms.Select(
                attrs={'class': 'js-complainant'})
        }

