from django.views.generic import *
from wkhtmltopdf.views import PDFTemplateView
from add_member.models import Person

# TODO: Move this view somewhere else. Maybe in the contact log app
# Views for the main site for the SPFA-MT application
class spfaView(TemplateView):
    template_name = 'index.html'


class PDFView(PDFTemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        return super(PDFView, self).get_context_data(
            pagesize="A4",
            cls=Person.objects.all(),
            title="Hi there!",
            **kwargs
        )
