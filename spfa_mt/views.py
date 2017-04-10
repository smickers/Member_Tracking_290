from django.views.generic import *
from add_member.models import Person

# TODO: Move this view somewhere else. Maybe in the contact log app
# Views for the main site for the SPFA-MT application
class spfaView(TemplateView):
    template_name = 'index.html'



