from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person
from .forms import PersonForm


# Create your views here.
class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm

class PersonList(ListView):
    model = Person
    template_name = 'add_member/person_list.html'

class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm

class PersonDetail(DetailView):
    model = Person
    template_name = 'add_member/person_detail.html'