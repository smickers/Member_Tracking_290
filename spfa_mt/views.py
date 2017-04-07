from django.views.generic import *


# Views for the main site for the SPFA-MT application
class spfaView(TemplateView):
    template_name = 'index.html'

