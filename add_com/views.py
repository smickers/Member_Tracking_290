from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Committee
from .forms import ComForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from drf_haystack.viewsets import HaystackViewSet
from serializer import CommitteeSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter


# View for Committee creation:
class ComCreate(SuccessMessageMixin, CreateView):
    model = Committee
    form_class = ComForm
    form = ComForm()
    success_url = reverse_lazy('add_com:committee_add')
    success_message = 'Committee created.'


# Creates the 'success' view
class ComCreateSuccess(DetailView):
    model = Committee
    template_name = 'add_com/committee_form.html'
    # # FUNCTION: get_context_data
    # # PURPOSE: Gets the context data from the previous page. In this case,
    # #           it gathers the primary key (pk)
    # # PARAMS: self ->
    # #         kwargs -> arguments being passed in. In this case, the PK.
    # def get_context_data(self, **kwargs):
    #     context = super(ComCreateSuccess, self).get_context_data(**kwargs)
    #     return context


# View for listing all Committees in the DB:
class ComList(ListView):
    model = Committee
    template_name = 'add_com/committee_list.html'


# View for showing details on a specific Committee:
class ComDetailView(DetailView):
    model = Committee
    template_name = 'add_com/committee_detail.html'

class CommitteeSearchView(HaystackViewSet):
    """
    View that connects the committee search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    index_models = [Committee]
    serializer_class = CommitteeSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]
