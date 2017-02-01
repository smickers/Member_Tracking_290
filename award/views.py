from django.shortcuts import render
from .models import EducationAward
from .forms import EducationAwardForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
###
# Views for Education Awards
###


class EducationAwardCreation(CreateView):
    model = EducationAward
    form_class = EducationAwardForm
    form = EducationAwardForm()

    def get_success_url(self):
        return self.object.get_absolute_url()


class EducationAwardCreationSuccess(DetailView):
    # Define the model
    model = EducationAward

    def get_context_data(self, **kwargs):
        context = super(EducationAwardCreationSuccess, self).get_context_data(**kwargs)
        return context