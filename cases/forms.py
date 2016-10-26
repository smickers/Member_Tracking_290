from django.forms import ModelForm, NumberInput, ValidationError
from cases.models import CaseMembers
from django import forms


class CaseMembersForm(ModelForm):
    caseNum = forms.CharField()
    memberNum = forms.CharField()
    class Meta:
        model = CaseMembers
        fields = ['caseNum', 'memberNum']
        labels = {
            'caseNum': 'CaseID',
            'memberNum' : 'MemberID',
        }