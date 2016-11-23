from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import CallerClass
from .forms import CaseMembersForm


# Create your views here.
class CaseMembersCreate(UpdateView):
    model = CallerClass
    form_class = CaseMembersForm
