from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person
from .forms import PersonForm


# view responsible for the member creation
class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm

#view for listing all the members found in the db
class PersonList(ListView):
    model = Person
    template_name = 'add_member/person_list.html'

#view for updating individual member info
class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm

#view for displaying individual member info
class PersonDetail(DetailView):
    model = Person
    template_name = 'add_member/person_detail.html'