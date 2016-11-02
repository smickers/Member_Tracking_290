from django.shortcuts import render
from .models import Case
from .forms import CaseForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CaseCreate(CreateView):
    model = Case
    form_class = CaseForm
