from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Event, Person
from .validators import *
from create_event.fields import ListTextWidget
from django import forms
from datetime import date


# This creates names for fields on the form.
class EventForm(ModelForm):

    # Name:     __init__
    # Function: This routine creates the datalist for selecting a location or entering it in.
    def __init__(self, *args, **kwargs):


        _location_list = {
            'Prince Albert',
            'Moose Jaw',
            'Regina',
            'Saskatoon'
        }
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['location'].widget = ListTextWidget(data_list=_location_list, name='location-list')
        # self.fields['members'].widget.attrs = {'class':'js-additional-members'}


    # This names the fields for the form
    class Meta:
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
        model = Event

        fields = '__all__'
        labels = {
            'Name:': 'name',
            'Description': 'description',
            'Date:': 'date',
            'Location': 'location'
        }

        widgets = {
            'date': SelectDateWidget(months=MONTHS, years=range(2010, datetime.datetime.now().year + 10)),
            'members': forms.SelectMultiple(
                attrs={'class':'js-members', 'style': 'width: 100%'})
        }



# This class creates the add member form for adding a member to an event.
class EventAddMemberForm(ModelForm):
    class Meta:
        model = Event
        fields = ('members',)

    # Name:     __init__
    # Function: Constructor for the add member form.
    def __init__(self, **kwargs):
        super(EventAddMemberForm, self).__init__(**kwargs)
        self.fields['members'].queryset = Person.objects.exclude(event_members=self.instance)

    # Name:     clean_members
    # Function: Cleans members to be saved to the DB.
    def clean_members(self):
        return self.initial['members'] | self.cleaned_data['members']


