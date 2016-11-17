from django.forms import ModelForm, NumberInput, ValidationError, SelectDateWidget
from .models import Event
from .validators import *

class EventForm(ModelForm):
    class Meta:
        model = Event

        fields = '__all__'
        labels = {
            '': '',
        }