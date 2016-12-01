from django.shortcuts import render
from .models import Event, Person
from .forms import EventForm, EventAddMemberForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView

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


class EventList(ListView):
    model = Event
    template_name = 'create_event/event_list.html'

class EventAddMember(UpdateView):
    model = Event
    form_class = EventAddMemberForm

class EventDetailView(DetailView):
    model = Event
    template_name = 'create_event/event_actual_detail.html'