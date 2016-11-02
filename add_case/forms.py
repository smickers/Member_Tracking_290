from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Case
import re
import datetime

class CaseForm(ModelForm):
    class Meta:
        model = Case

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
            'date': SelectDateWidget()
        }

        def clean_date(self):
            data = self.cleaned_data['date']
            if data < datetime.datetime.now().date():
                raise ValidationError("Date cannot be in the future")
            return data
