from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Event
from .validators import *
from create_event.fields import ListTextWidget
from django import forms


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        _location_list = {
            'Prince Albert',
            'Moose Jaw',
            'Regina',
            'Saskatoon'
        }
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['location'].widget = ListTextWidget(data_list=_location_list, name='location-list')

    class Meta:
        model = Event

        fields = '__all__'
        labels = {
            'Name:': 'name',
            'Description': 'description',
            'Date:': 'date',
            'Location': 'location'
        }
