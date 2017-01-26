from django.shortcuts import render
from .models import Meeting
from .forms import MeetingForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

# Class: MeetingCreation
# Purpose: Links our creation form to a meeting to be shown when the user
# wants to create a new meeting
class MeetingCreation(CreateView):
    # Link Meeting to the appropriate meeting form
    model = Meeting
    form_class = MeetingForm
    form = MeetingForm()


# Class: MeetingSuccess
# Purpose: The view that is shown upon successfully creating a meeting
class MeetingSuccess(DetailView):
    # Define the model
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super(MeetingSuccess, self).get_context_data(**kwargs)
        return context

