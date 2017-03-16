# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import contactLog
from .forms import ContactLogForm, ContactLogDetailsForm
from rest_framework import viewsets
from .serializers import ContactLogSerializer
import django_filters.rest_framework
import rest_framework_filters as filters


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

class ContactLogFilter(filters.FilterSet):
    date_gt = filters.DateFilter(name='date', lookup_expr='gt')
    date_lt = filters.DateFilter(name='date', lookup_expr='lt')
    empty_desc_filter = filters.CharFilter(name='description', lookup_expr='isnull')


    class Meta:
        model = contactLog

        fields = {
            'id': '__all__',
            'member': '__all__',
            'date': '__all__',
            'description': '__all__',
            'contactCode': '__all__',
            'date_gt': '__all__',
            'date_lt': '__all__',
        }


class ContactLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = contactLog.objects.all()
    serializer_class = ContactLogSerializer
    filter_class = ContactLogFilter

    filter_fields = ['id', 'member', 'date', 'description', 'contactCode', 'date_gt', 'date_lt']
