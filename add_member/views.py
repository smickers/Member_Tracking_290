from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person, PersonFile
from .forms import PersonForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer, MemberFileSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from rest_framework import generics, decorators
from spfa_mt.settings import MAX_FILE_SIZE
from rest_framework.exceptions import APIException
from django.db.models import ObjectDoesNotExist
from rest_framework.response import Response
from excel_to_json import convert_excel_json


# view responsible for the member creation
class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm

#view for listing all the members found in the db
class PersonList(ListView):
    model = Person
    template_name = 'add_member/person_list.html'

#view for updating individual member info
class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm

#view for displaying individual member info
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


class FileListCreateView(generics.ListCreateAPIView):
    queryset = PersonFile.objects.all()
    serializer_class = MemberFileSerializer

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        if file_obj.size > MAX_FILE_SIZE:
            raise FileTooLarge
        return super(FileListCreateView, self).post(request, *args, **kwargs)

class FileTooLarge(APIException):
    status_code = 400
    default_detail = 'File too large bruh'
    default_code = 'bad request'


class MemberFileUploadView(TemplateView):
    template_name ='add_member/memberbulkcreate.html'



@decorators.api_view(['GET'])
def excel_to_json(request, *args, **kwargs):
    """
    This is how you do a comment :) :) :) *wink* *WINK*
    """
    try:
        sample_file = PersonFile.objects.get(pk=kwargs['pk'])
        result = convert_excel_json(sample_file.file.file)
        return Response({"count": len(result), "Result": result})
    except ObjectDoesNotExist:
        return Response({"Error": "There is an error on parsing the excel file"})
    except IOError:
        return Response({'Error': 'File cannot be found'})
    except ValueError:
        return Response({'Error': 'Expects a pk'})
