# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import contactLog
from .forms import ContactLogForm, ContactLogDetailsForm
from rest_framework import viewsets
from .serializers import ContactLogSerializer
import django_filters.rest_framework
from add_case.models import Case
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

# Class:    ContactLogFilter
# Purpose:  Set up filtration options for contact logs.
class ContactLogFilter(filters.FilterSet):
    # Declaring filters for date ranges and empty descriptions
    date_gt = filters.DateFilter(name='date', lookup_expr='gt')
    date_lt = filters.DateFilter(name='date', lookup_expr='lt')
    empty_desc_filter = filters.CharFilter(name='description', lookup_expr='isnull')
    description = filters.CharFilter(name='description', lookup_expr='icontains')
    member__firstName = filters.CharFilter(name='member__firstName', lookup_expr='icontains')
    member__lastName = filters.CharFilter(name='member__lastName', lookup_expr='icontains')
    member__middleName = filters.CharFilter(name='member__middleName', lookup_expr='icontains')
    relatedCase_filter = filters.ModelChoiceFilter(name='relatedCase', method='filter_contact_logs_related_cases', queryset=contactLog.objects.all())
    # relatedCase_filter = filters.AllValuesFilter(name='relatedCase__id', lookup_expr='isnull')
    # case = filters.CharFilter(name='relatedCase__id')

    # Function:
    def filter_contact_logs_related_cases(self, queryset, name, value):
        # return contactLog.objects.all().filter(relatedCase__isnull=True)
        return queryset.filter(relatedCase__isnull=True)


    class Meta:
        model = contactLog

        # fields = {
        #     'id': '__all__',
        #     'member': '__all__',
        #     'date': '__all__',
        #     'description': '__all__',
        #     'contactCode': '__all__',
        #     'date_gt': '__all__',
        #     'date_lt': '__all__',
        # }
        fields = ['id', 'member', 'date', 'description', 'contactCode', 'relatedCase']


# Class:    ContactLogViewSet
# Purpose:  Setting up a view for serialized contact logs while allowing for filtering contact logs.
class ContactLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = contactLog.objects.all()
    serializer_class = ContactLogSerializer
    filter_class = ContactLogFilter

    filter_fields = ['id', 'member', 'date', 'description', 'contactCode', 'date_gt', 'date_lt']
