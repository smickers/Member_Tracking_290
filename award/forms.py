from django.forms import ModelForm
from .models import EducationAward


###
# Form for creating an Education Award:
###
class EducationAwardForm(ModelForm):

    class Meta:
        model = EducationAward
        fields = '__all__'
        labels = {
            'description': 'Description',
            'award_amount': 'Award Amount'
        }
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