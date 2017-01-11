from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Committee
from .forms import ComForm


# View for Committee creation:
class ComCreate(CreateView):
    model = Committee
    form_class = ComForm
    form = ComForm()


# View for listing all Committees in the DB:
class ComList(ListView):
    model = Committee
    template_name = 'add_com/com_list.html'


# Creates the 'success' view
class ComCreateSuccess(DetailView):
    model = Committee

    # FUNCTION: get_context_data
    # PURPOSE: Gets the context data from the previous page. In this case,
    #           it gathers the primary key (pk)
    # PARAMS: self ->
    #         kwargs -> arguments being passed in. In this case, the PK.
    def get_context_data(self, **kwargs):
        context = super(ComCreateSuccess, self).get_context_data(**kwargs)
        return context


class ComDetailView(DetailView):
    model = Committee
    template_name = 'add_com/com_detail.html'
