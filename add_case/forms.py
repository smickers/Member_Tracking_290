from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Case
import re

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

