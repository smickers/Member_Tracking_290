# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import contactLog
from .forms import ContactLogForm, ContactLogDetailsForm
from rest_framework import viewsets
from .serializers import ContactLogSerializer


# View ContactLogCreate
# Purpose: Put together a form to allow the user to create a new
# contact log from.
class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm


class ContactLogEdit(UpdateView):
    model = contactLog
    form_class = ContactLogForm


class ContactLogDetails(DetailView):
    model = contactLog
    form_class = ContactLogDetailsForm


class ContactLogList(ListView):
    model = contactLog

class ContactLogViewSet(viewsets.ModelViewSet):
    queryset = contactLog.objects.all().order_by("id")
    serializer_class = ContactLogSerializer

