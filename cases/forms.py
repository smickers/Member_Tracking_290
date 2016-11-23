from django.forms import ModelForm, NumberInput, ValidationError
from django import forms
from add_case.models import Case

class CaseMembersForm(ModelForm):
    class Meta:
        model = Case
        fields = ['additionalMembers']

        labels = {
            'additionalMembers':'Additional Involved Persons',
        }