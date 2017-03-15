# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import contactLog
from .forms import ContactLogForm, ContactLogDetailsForm
from rest_framework import viewsets
from .serializers import ContactLogSerializer
import django_filters.rest_framework
from itertools import chain
from operator import attrgetter


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


class ContactLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactLogSerializer
    queryset = contactLog.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


    def get_queryset(self):

        # previous_was_and = False
        # previous_was_or = False
        # all_contact_logs = contactLog.objects.all()
        # curr_query_set = contactLog.objects.all()
        # #query_set_to_return = contactLog.objects.filter(id=-1)
        # for key, value in self.request.GET.items():
        #     print('[' + key + '] => [' + value + ']')
        #     if key[:2] == "id":
        #         if previous_was_or is True:
        #             curr_query_set = curr_query_set | all_contact_logs.filter(id=value)
        #             # print(len(curr_query_set))
        #             previous_was_or = False
        #         else:
        #             print("Running else stmnt!")
        #             curr_query_set = curr_query_set.filter(id=value)
        #     elif key == "date":
        #         if previous_was_or:
        #             curr_query_set = curr_query_set | all_contact_logs.filter(date=value)
        #             previous_was_or = False
        #         else:
        #             curr_query_set = curr_query_set.filter(date=value)
        #     elif key == "description":
        #         if previous_was_or:
        #             curr_query_set = curr_query_set | all_contact_logs.filter(description=value)
        #             previous_was_or = False
        #         else:
        #             curr_query_set = curr_query_set.filter(description=value)
        #     elif key == "contactCode":
        #         if previous_was_or:
        #             curr_query_set = curr_query_set | all_contact_logs.filter(contactCode=value)
        #             previous_was_or = False
        #         else:
        #             curr_query_set = curr_query_set.filter(contactCode=value)
        #     elif key == "operator" and value == "OR":
        #         print("Setting previous to true")
        #         previous_was_or = True
        #
        #
        #     # print(value)
        #     #
        #     # print("NEXT:")
        #

        queryset = contactLog.objects.all()
        base_query_set = contactLog.objects.filter(id=1)
        cl_id = self.request.query_params.get('id', None)
        cl_date = self.request.query_params.get('date', None)
        cl_desc = self.request.query_params.get('description', None)
        cl_cc = self.request.query_params.get('contactCode', None)

        if cl_id is not None:
            queryset = contactLog.objects.filter(id=cl_id)
        if cl_date is not None:
            queryset = queryset.filter(date=cl_date)
        if cl_desc is not None:
            queryset = queryset.filter(description=cl_desc)
        if cl_cc is not None:
            queryset = queryset.filter(contactCode=cl_cc)

        #final_queryset = sorted(list(chain(queryset, base_query_set)), key=attrgetter('id'))
        return queryset# | base_query_set
        # return curr_query_set
