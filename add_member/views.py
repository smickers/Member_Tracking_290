from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Person

# Create your views here.

class PersonCreate(CreateView):
    person = Person
    template_name='add_member/person_form.html'
    fields = ['memberID', 'firstName', 'middleName', 'socNum',
              'city', 'mailAddress', 'mailAddress2', 'pCode',
              'bDay', 'gender', 'hPhone', 'cPhone', 'hEmail',
              'campus', 'jobType', 'committee', 'memberImage']
    def get_queryset(self):
            return Person.objects.all()