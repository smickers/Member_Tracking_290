from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person
from .forms import PersonForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from spfa_mt import settings
from wsgiref.util import FileWrapper
from mimetypes import MimeTypes
from django.http import HttpResponse
import os.path



# view responsible for the member creation
class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm


# view for listing all the members found in the db
class PersonList(ListView):
    model = Person
    template_name = 'add_member/person_list.html'


# view for updating individual member info
class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm


# view for displaying individual member info
class PersonDetail(DetailView):
    model = Person
    template_name = 'add_member/person_detail.html'


class MemberSearchView(HaystackViewSet):
    """
    View that connects the Member search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    index_models = [Person]
    serializer_class = MemberSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]

# TODO: Follow this link for downloadi file stuff
# http://stackoverflow.com/questions/15246661/downloading-the-fileswhich-are-uploaded-from-media-folder-in-django-1-4-3
def download(request, file_name):

    mime = MimeTypes()

    file_path = settings.MEDIA_ROOT + file_name
    file_wrapper = FileWrapper(file(file_path, 'rb'))
    file_mimetype = mime.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name)

    return response
