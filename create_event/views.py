from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    location_list = ('REGINA', 'SASKATOON', 'MOOSE JAW', 'PRINCE ALBERT')
    form = EventForm(data_list=location_list)
