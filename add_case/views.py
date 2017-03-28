from .models import Case
from .forms import CaseForm
from django.views.generic import *
from django.views.generic.edit import *
from drf_haystack.viewsets import HaystackViewSet
from serializer import CaseSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from grievance_award_creation.models import GrievanceAward
from django.core.exceptions import ObjectDoesNotExist


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
    form_class = CaseForm


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