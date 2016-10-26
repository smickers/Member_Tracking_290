from django.forms import ModelForm, NumberInput, ValidationError
from cases.models import CaseMembers


class CaseMembersForm(ModelForm):
    class Meta:
        model = CaseMembers
        fields = ['caseNum', 'memberNum']
        labels = {
            'caseNum': 'CaseID',
            'memberNum' : 'MemberID',
        }