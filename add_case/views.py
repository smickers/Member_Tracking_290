from .models import Case
from .forms import CaseForm
from django.views.generic import *
from django.views.generic.edit import *
from drf_haystack.viewsets import HaystackViewSet
from serializer import CaseSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from grievance_award_creation.models import GrievanceAward
from django.core.exceptions import ObjectDoesNotExist
from contact_log.models import contactLog
import rest_framework_filters as filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.core.validators import EMPTY_VALUES


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
            context['grievance_award'] = GrievanceAward.objects.get(pk=self.kwargs['pk'])
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

class FilterOffsetClass(LimitOffsetPagination):
    """
    This is our offset. It overwrites what we have in the settings page.
    """
    try:
        default_limit = Case.objects.all().count()
    except Exception as e:
        default_limit = 100

# View to set up case filter options
class CaseFilter(filters.FilterSet):
    # Setting up the filters for date ranges
    date_before = filters.DateFilter(name='date', lookup_expr='before')
    date_after = filters.DateFilter(name='date', lookup_expr='after')
    # Filters for complainants by firstName, lastName, and blank
    cn_fn = filters.CharFilter(name='complainant__firstName', lookup_expr='icontains')
    cn_ln = filters.CharFilter(name='complainant__lastName', lookup_expr='icontains')
    # Satellites field is left blank or is null
    sat_blank = EmptyStringFilter(name='satellite')
    sat = filters.CharFilter(name='satellite', lookup_expr='icontains')

    class Meta:
        model = Case
        fields = {'id': '__all__',
                  'lead': '__all__',
                  'complainant': '__all__',
                  'campus': '__all__',
                  'satellite': '__all__',
                  'school': '__all__',
                  'program': '__all__',
                  'department': '__all__',
                  'caseType': '__all__',
                  'status': '__all__',
                  'additionalMembers': '__all__',
                  'additionalNonMembers': '__all__',
                  'date': '__all__'}


# View to allow serialized cases ... essentially, what allows our filtering to happen.
class CaseFilterView(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSearchSerializer
    filter_class = CaseFilter
    filter_fields = ['id', 'lead', 'complainant' 'campus', 'satellite', 'school',
                  'program', 'department', 'caseType', 'status', 'additionalMembers',
                  'additionalNonMembers', 'date_before', 'date_after']
    pagination_class = FilterOffsetClass
