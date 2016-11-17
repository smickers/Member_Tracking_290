from django.forms import ModelForm, NumberInput, ValidationError
from cases.models import CaseMembers, CallerClass
from django import forms


class CaseMembersForm(ModelForm):
    caseNum = forms.CharField()
    memberNum = forms.CharField()
    class Meta:
        model = CallerClass
        fields = ['caseNum', 'memberNum']
        labels = {
            'caseNum': 'CaseID',
            'memberNum' : 'MemberID',
        }