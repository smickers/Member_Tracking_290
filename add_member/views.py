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


# Follow this link for downloading file stuff
# http://stackoverflow.com/questions/15246661/downloading-the-fileswhich-are-uploaded-from-media-folder-in-django-1-4-3
# FUNCTION: download
# PURPOSE:  Overrides the existing download functionality to define where a user will download files from.
# PARAMS:   request -> the HTTPRequest object sent to the client.
#           file_name-> the name of the file to download
def download(request, file_name):
    mime = MimeTypes()
    file_path = settings.MEDIA_ROOT + file_name
    file_wrapper = FileWrapper(file(file_path, 'rb'))
    file_mimetype = mime.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name)
    response['Content-Length'] = len(response.content)
    return response
