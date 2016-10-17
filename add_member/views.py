from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person


# Create your views here.
class PersonCreate(CreateView):
    model = Person
    fields = ['memberID', 'firstName', 'middleName', 'socNum',
              'city', 'mailAddress', 'mailAddress2', 'pCode',
              'bDay', 'gender', 'hPhone', 'cPhone', 'hEmail',
              'campus', 'jobType', 'committee', 'memberImage']
