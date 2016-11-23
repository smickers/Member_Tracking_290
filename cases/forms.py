from django.forms import ModelForm, NumberInput, ValidationError
from cases.models import CaseMembers, CallerClass
from django import forms
from add_case.models import Case

class CaseMembersForm(ModelForm):
    # caseNum = forms.CharField()
    # memberNum = forms.CharField()
    class Meta:
        model = Case
        fields = ['additionalMembers']
