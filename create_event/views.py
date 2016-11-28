from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# This assigns the model, the form class and the form.
class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    form = EventForm()


# This class creates the success view.
class EventCreateSuccess(DetailView):
    model = Event

    # Name:     get_context_data
    # Purpose: Gets the context data from the previous page.
    #           In this case, it grabs the primary key.
    # params:   self
    #           **kwargs - arguments being passed in (primary key)
    def get_context_data(self, **kwargs):
        context = super(EventCreateSuccess, self).get_context_data(**kwargs)
        return context
