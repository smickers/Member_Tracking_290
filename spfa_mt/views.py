from django.views.generic import *
from easy_pdf.views import PDFTemplateView
from add_member.models import Person

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
