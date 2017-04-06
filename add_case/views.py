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