# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import contactLog
from .forms import ContactLogForm
from django.http import HttpResponse
from django.template import loader
from drf_haystack.viewsets import HaystackViewSet
from add_member.serializer import MemberSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from add_member.models import Person

# View success
# Purpose: This view will be called whenever a contact log has
# been successfully created. It will display a success page with
# the new contact log's PK.
def success(request, pk):
    template = loader.get_template('contact_log/success.html')
    context = {
        'pk': int(pk)
    }

    return HttpResponse(template.render(context, request))

# View ContactLogCreate
# Purpose: Put together a form to allow the user to create a new
# contact log from.
class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogUpdate(UpdateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogList(ListView):
    model = contactLog


#class ContactLogSearchView(HaystackViewSet):
    """
    View that connects the Member search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    # index_models = [Person]
    # serializer_class = MemberSearchSerializer
    # filter_backends = [HaystackAutocompleteFilter]
