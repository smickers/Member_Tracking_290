from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    form = EventForm()

class EventCreateSuccess(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventCreateSuccess, self).get_context_data(**kwargs)
        return context
