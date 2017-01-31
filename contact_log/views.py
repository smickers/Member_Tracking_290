# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import contactLog
from .forms import ContactLogForm

# View ContactLogCreate
# Purpose: Put together a form to allow the user to create a new
# contact log from.
class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogEdit(UpdateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogList(ListView):
    model = contactLog