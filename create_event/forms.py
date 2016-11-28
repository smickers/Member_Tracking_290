from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Event
from .validators import *
from create_event.fields import ListTextWidget
from django import forms


class EventForm(ModelForm):
    char_field_with_list = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        _location_list = kwargs.pop('data_list', None)
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_location_list, name='location-list')

    class Meta:
        model = Event

        fields = '__all__'
        labels = {
            'Name:': 'name',
            'Description': 'description',
            'Date:': 'date',
            'Location': 'location'
        }
