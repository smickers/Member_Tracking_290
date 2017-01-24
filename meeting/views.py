from django.shortcuts import render
from .models import MeetingCreation
from .forms import MeetingForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
class MeetingCreation(CreateView):
    # Link GrievanceAward to the appropriate grievance award form
    model = MeetingCreation
    form_class = MeetingForm
    form = MeetingForm()

# Class: GrievanceAwardCreationSuccess
# Purpose: The view that is shown upon successfully creating a grievance award.
class MeetingSuccess(DetailView):
    # Define the model
    model = MeetingCreation

    def get_context_data(self, **kwargs):
        context = super(MeetingSuccess, self).get_context_data(**kwargs)
        return context