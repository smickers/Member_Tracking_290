from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import contactLog
from .forms import ContactLogForm
from . import models
from django.http import HttpResponse
from django.template import loader

def success(request, pk):
    template = loader.get_template('contactLog/success.html')
    context = {
        'pk': int(pk)
    }

    return HttpResponse(template.render(context, request))


def contactLogCreateSuccess(request):
    template = loader.get_template('contactLog/success.html')
    context = {
        'contactLogID': '55'
    }
    return HttpResponse(template.render(context, template))

class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm

class CreateSuccess(DetailView):
    model = contactLog
    pk = 5
    template_name = 'contactLog/success.html'

