from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Committee
from .forms import ComForm


# View for Committee creation:
class ComCreate(CreateView):
    model = Committee
    form_class = ComForm


# View for listing all Committees in the DB:
class ComList(ListView):
    model = Committee
    template_name = 'add_com/com_list.html'

