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
    # Purpose:  Gets the context data from the previous page.
    #           In this case, it grabs the primary key.
    # params:   self
    #           **kwargs - arguments being passed in (primary key)
    def get_context_data(self, **kwargs):
        context = super(EventCreateSuccess, self).get_context_data(**kwargs)
        return context

# This class declares the template for the Event List
class EventList(ListView):
    model = Event
    template_name = 'create_event/event_list.html'

# This class declares the form for the Adding a member
class EventAddMember(UpdateView):
    model = Event
    form_class = EventAddMemberForm

# This class declares a template for the Detail view for an Event
class EventDetailView(DetailView):
    model = Event
    template_name = 'create_event/event_actual_detail.html'

# This class declares the form for the editing an event
class EventEditView(UpdateView):
    model = Event
    form_class = EventForm
