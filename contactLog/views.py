from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import contactLog
from .forms import ContactLogForm


# Create your views here.
class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm