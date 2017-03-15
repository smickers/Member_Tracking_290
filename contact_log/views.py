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
    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)



    # def get_queryset(self):
    #
    #     queryset = contactLog.objects.all()
    #     base_query_set = contactLog.objects.filter(id=1)
    #     cl_id = self.request.query_params.get('id', None)
    #     cl_date = self.request.query_params.get('date', None)
    #     cl_desc = self.request.query_params.get('description', None)
    #     cl_cc = self.request.query_params.get('contactCode', None)
    #
    #     if cl_id is not None:
    #         queryset = contactLog.objects.filter(id=cl_id)
    #     if cl_date is not None:
    #         queryset = queryset.filter(date=cl_date)
    #     if cl_desc is not None:
    #         queryset = queryset.filter(description=cl_desc)
    #     if cl_cc is not None:
    #         queryset = queryset.filter(contactCode=cl_cc)
    #
    #     #final_queryset = sorted(list(chain(queryset, base_query_set)), key=attrgetter('id'))
    #     return queryset# | base_query_set
        # return curr_query_set
