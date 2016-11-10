from django.views.generic.edit import CreateView
from .models import contactLog
from .forms import ContactLogForm
from django.http import HttpResponse
from django.template import loader

# View success
# Purpose: This view will be called whenever a contact log has
# been successfully created. It will display a success page with
# the new contact log's PK.
def success(request, pk):
    template = loader.get_template('contactLog/success.html')
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

