from django.forms import ModelForm, SelectDateWidget
from datetime import date
from .models import EducationAward, PDAward
from django import forms


###
# Form for creating an Education Award:
###
class EducationAwardForm(ModelForm):

    # Does the bulk of the heavy lifting
    class Meta:
        model = EducationAward
        fields = '__all__'
        labels = {
            'description': 'Description',
            'award_amount': 'Award Amount'
        }
        # Custom error messages, when errors are thrown:
        error_messages = {
            'description': {
                'required': 'An award description is required.',
                'max_length': 'Award description cannot exceed 150 characters in length.',
                'min_length': 'Award description cannot be left blank.'
            },
            'award_amount': {
                'required': 'An award value is required.',
                'invalid': 'Award value must be a whole number (no decimals).',
                'max_value': 'Amount must be greater than $0 and less than $10,000.',
                'min_value': 'Amount must be greater than $0 and less than $10,000.'
            }
        }

class PDAwardForm(ModelForm):
    class Meta:
        model=PDAward
        fields='__all__'
        labels={
            'awardName':'Award Name',
            'memberAwarded':'Member Awarded',
            'awardCost':'Award Cost',
            'startDate': 'Start Date',
            'endDate': 'End Date'
        }
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
        widgets = {
            'startDate': SelectDateWidget(months=MONTHS),
            'endDate': SelectDateWidget(months=MONTHS),
            'memberAwarded': forms.Select(
                attrs={'class': 'js-membersAwarded'}),
        }

    #def clean(self):
    #    form_startDate = self.cleaned_data.get('startDate')
     #   form_endDate = self.cleaned_data.get('endDate')
     #   if form_endDate < form_startDate:
     #       raise forms.ValidationError("End Date must be the same as or come after start date")