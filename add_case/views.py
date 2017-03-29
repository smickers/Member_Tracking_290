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


# View to set up case filter options
class CaseFilter(filters.FilterSet):
    # Setting up the filters for date ranges
    date_before = filters.DateFilter(name='date', lookup_expr='before')
    date_after = filters.DateFilter(name='date', lookup_expr='after')
    # Filters for complainants by firstName, lastName, and blank
    cn_fn = filters.CharFilter(name='complainant__firstName', lookup_expr='with')
    cn_ln = filters.CharFilter(name='complainant__lastName', lookup_expr='with')
    # Satellites field is left blank or is null
    sat_blank = filters.CharFilter(name='satellite', lookup_expr='isnull')


    class Meta:
        model = Case
        fields = ['id', 'lead', 'complainant', 'campus', 'satellite', 'school',
                  'program', 'department', 'caseType', 'status', 'additionalMembers',
                  'additionalNonMembers', 'date']


# View to allow serialized cases ... essentially, what allows our filtering to happen.
class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSearchSerializer
    filter_class = CaseFilter
    filter_fields = ['id', 'lead', 'complainant' 'campus', 'satellite', 'school',
                  'program', 'department', 'caseType', 'status', 'additionalMembers',
                  'additionalNonMembers', 'date_before', 'date_after']