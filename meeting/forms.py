from django.forms import ModelForm, SelectDateWidget, Textarea, RadioSelect, TextInput, NumberInput
from .models import MeetingCreation
from datetime import date
from django import forms

class MeetingForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MeetingCreation

        # Date range is +- 5 years

        # Make the range +6 on the high end, because this function doesn't
        # include the end range value
        YEARS = range(date.today().year - 5, date.today().year + 6)
        YEARS.sort()

        # Define months so they're entered as three letters
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

        # Show all fields and set up labels
        fields = '__all__'
        labels = {
            'committee': 'Committee',
            'spfa_liason': 'SPFA Liason',
            'members_attending': 'Memberes Attending',
            'description': 'Description',
            'date': 'Meeting Date'
        }

        # Use some special widgets for certain fields
        widgets = {
            'date': SelectDateWidget(months=MONTHS, years=YEARS),
            'description': Textarea(),
        }

