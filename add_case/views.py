from .models import Case
from .forms import CaseForm
from django.views.generic import *
from django.views.generic.edit import *
from drf_haystack.viewsets import HaystackViewSet
from serializer import CaseSearchSerializer, CaseFilterSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from grievance_award_creation.models import GrievanceAward
from django.core.exceptions import ObjectDoesNotExist
from contact_log.models import contactLog
import rest_framework_filters as filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.core.validators import EMPTY_VALUES
from rest_framework import serializers


class CaseCreate(CreateView):
    model = Case
    form_class = CaseForm


class CaseSearchView(HaystackViewSet):
    """
    View that connects the Member search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    index_models = [Case]
    serializer_class = CaseSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]


class UpdateCaseView(UpdateView):
    model = Case
    template_name = 'add_case/case_form.html'
    context_object_name = 'case'
    form_class = CaseForm

    def get_context_data(self, **kwargs):
        context = super(UpdateCaseView, self).get_context_data(**kwargs)
        try:
            # context['related_contact_logs'] = contactLog.objects.get(relatedCase__pk=self.kwargs['pk'])
            context['related_contact_logs'] = contactLog.objects.all().filter(relatedCase__pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            pass

        return context


# view for displaying individual member info
class CaseDetail(DetailView):
    model = Case
    template_name = 'add_case/cases_detail.html'
    context_object_name = 'case'

    def get_context_data(self, **kwargs):
        context = super(CaseDetail, self).get_context_data(**kwargs)
        try:
            #   will get all the field names of the case model
            fields = [f.name for f in Case._meta.get_fields()]
            context['fields'] = fields
            context['grievance_award'] = GrievanceAward.objects.get(pk=self.kwargs['pk'])
            context['contact_log'] = contactLog.objects.filter(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            pass

        return context


# view for listing all the members found in the db
class CaseList(ListView):
    model = Case
    template_name = 'add_case/cases_list.html'


class EmptyStringFilter(filters.BooleanFilter):
    """
    Writing a custom filter so we can get all results with empty strings.
    """
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.name: ""})


# View to set up case filter options
class CaseFilter(filters.FilterSet):
    # Filters for complainants by firstName, lastName, and blank
    complainant__firstName = filters.CharFilter(name='complainant__firstName', lookup_expr='icontains')
    complainant__lastName = filters.CharFilter(name='complainant__lastName', lookup_expr='icontains')
    school = filters.CharFilter(name='school', lookup_expr='contains')
    program = filters.CharFilter(name='program', lookup_expr='contains')
    campus = filters.CharFilter(name='campus', lookup_expr='icontains')
    department = filters.CharFilter(name='department', lookup_expr='contains')
    status = filters.CharFilter(name='status', lookup_expr='contains')
    # Setting up the filters for date ranges
    date_before = filters.DateFilter(name='date', lookup_expr='gte')
    date_after = filters.DateFilter(name='date', lookup_expr='lte')

    # Satellites field is left blank or is null
    sat_blank = EmptyStringFilter(name='satellite')
    sat = filters.CharFilter(name='satellite', lookup_expr='icontains')

    class Meta:
        model = Case
        fields = ['id', 'lead', 'complainant', 'campus', 'satellite', 'school',
                  'program', 'department', 'caseType', 'status', 'additionalMembers',
                  'additionalNonMembers', 'date']


class FilterOffsetClass(LimitOffsetPagination):
    """
    This is our offset. It overwrites what we have in the settings page.
    """
    try:
        default_limit = Case.objects.all().count()
    except Exception as e:
        default_limit = 100


# View to allow serialized cases ... essentially, what allows our filtering to happen.
class CaseFilterView(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseFilterSerializer
    filter_class = CaseFilter
    filter_fields = ['id', 'lead', 'complainant', 'campus', 'satellite', 'school',
                     'program', 'department', 'caseType', 'status', 'additionalMembers',
                     'additionalNonMembers', 'date']
    pagination_class = FilterOffsetClass
