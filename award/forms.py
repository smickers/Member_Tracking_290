from django.forms import ModelForm, SelectDateWidget, TextInput
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
        fields = ('description', 'awardAmount')
        labels = {
            'description': 'Description',
            "awardAmount": 'Award Amount'
        }
        # Custom error messages, when errors are thrown:
        error_messages = {
            'description': {
                'required': 'An award description is required.',
                'max_length': 'Award description cannot exceed 150 characters in length.',
                'min_length': 'Award description cannot be left blank.'
            },
            "awardAmount": {
                'required': 'An award value is required.',
                'invalid': 'Award value must be a whole number (no decimals).',
                'max_value': 'Amount must be greater than $0 and less than $10,000.',
                'min_value': 'Amount must be greater than $0 and less than $10,000.'
            }
        }


class EducationAwardUpdateForm(ModelForm):

    # Does the bulk of the heavy lifting
    class Meta:
        model = EducationAward
        fields = '__all__'
        labels = {
            'description': 'Description',
            "awardAmount": 'Award Amount',
            'awardedMember': 'Awarded Member',
            'awardRecipient' : 'Award Recipient',
            'awardType' : 'Award Type',
            'yearAwarded' : 'Year',
        }
        # Custom error messages, when errors are thrown:
        error_messages = {
            'description': {
                'required': 'An award description is required.',
                'max_length': 'Award description cannot exceed 150 characters in length.',
                'min_length': 'Award description cannot be left blank.'
            },
            "awardAmount": {
                'required': 'An award value is required.',
                'invalid': 'Award value must be a whole number (no decimals).',
                'max_value': 'Amount must be greater than $0 and less than $10,000.',
                'min_value': 'Amount must be greater than $0 and less than $10,000.'
            }
        }
        widgets={
            'description': TextInput(attrs={'readonly':'readonly'}),
            "awardAmount": TextInput(attrs={'readonly':'readonly'}),
            'awardedMember': forms.Select(
                attrs={'class': 'js-eduAward', 'style': 'width: 100%'}),
        }


class PDAwardForm(ModelForm):
    class Meta:
        model=PDAward
        fields='__all__'
        labels={
            'awardName':'Description',
            'memberAwarded':'Member Awarded',
            'awardCost':'Cost',
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
                attrs={'class': 'js-membersAwarded', 'style': 'width: 100%'}),
        }