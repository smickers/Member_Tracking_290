from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import CaseMembers
from .forms import CaseMembersForm


# Create your views here.
class CaseMembersCreate(CreateView):
    model = CaseMembers
    form_class = CaseMembersForm