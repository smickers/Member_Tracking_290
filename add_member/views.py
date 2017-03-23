from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person, PersonFile
from .forms import PersonForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer, MemberFileSerializer, MemberSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from rest_framework import decorators
from spfa_mt.settings import MAX_FILE_SIZE
from rest_framework.exceptions import APIException
from django.db.models import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import generics, status
from excel_to_json import convert_excel_json
from exceptions import ValueError
import json
import gc
from django.core.exceptions import ValidationError

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
    """
        View that's responsible for accepting a file and writing it into the database
    """

    queryset = PersonFile.objects.all()
    serializer_class = MemberFileSerializer


    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        if file_obj.size > MAX_FILE_SIZE:
            raise FileTooLarge
        return super(FileListCreateView, self).post(request, *args, **kwargs)



class MemberFileUploadView(TemplateView):
    """
        Renders template for the Member Bulk Create page.
    """
    template_name ='add_member/memberbulkcreate.html'



@decorators.api_view(['GET'])
def excel_to_json(request, *args, **kwargs):
    """
        Function-based view responsible for calling the function that converts the excel content to json.
        @:return JSON response that includes the following key/value pairs
                    * count: count of the member info found in the excel sheet
                    * Result: Array of key/val pair that contains each member info found in the excel sheet.
    """
    try:
        sample_file = PersonFile.objects.get(pk=kwargs['pk'])  # get the PersonFile object using the pk
        result = convert_excel_json(sample_file.file.file)  # convert the excel file to json string
        return Response({"count": len(result), "Result": result})  # return a JSON reponse
    except ObjectDoesNotExist:
        return Response({"Error": "There is an error on parsing the excel file"})
    except IOError:
        return Response({'Error': 'File cannot be found'})
    except ValueError:
        return Response({'Error': 'Expects a pk'})

@decorators.api_view(['POST'])
def json_to_members(request, *args, **kwargs):

    json_results = json.loads(request.body)
    sample_file = PersonFile.objects.get(pk=json_results['pk'])
    json_repr = convert_excel_json(sample_file.file.file)

    try:
        for member in json_repr:
            serializer = MemberSerializer(data=member)
            if not serializer.is_valid():
                print(serializer.errors)
                raise AssertionError('The excel sheet contains invalid fields. '
                                     'Please check the sheet and upload it again')
            gc.collect()

        for member in json_repr:
            serializer = MemberSerializer(data=member)
            print(serializer)
            serializer.is_valid()
            serializer.save()
    except AssertionError as e:
        return Response({'Error': str(e)}, status.HTTP_406_NOT_ACCEPTABLE)
    except ValidationError as e:
        return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    return Response({'Detail': 'Success', 'count': len(json_repr)}, status.HTTP_201_CREATED)

class FileTooLarge(APIException):
    """
        This exceptions gets raised if the file uploaded is exceeding the file size limit
    """
    status_code = 400
    default_detail = 'The file exceeded the file size limit. Please upload a smaller file'
    default_code = 'bad request'

