from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person, PersonFile
from .forms import PersonForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from .models import Person
from .forms import PersonForm, MemberFilterForm
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
from spfa_mt import settings
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
import rest_framework_filters as filters
from contact_log.models import contactLog
from spfa_mt import settings
from wsgiref.util import FileWrapper
from mimetypes import MimeTypes
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

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

    # FUNCTION: get_context_data()
    # PURPOSE: Allows us to return data regarding contact logs related to the member we are currently viewing.
    # PARAMS:  **kwargs -> argument to be passed to the filter. In this case, is is the current member's PK.
    # RETURNS: Context in which the filtered items exist (readable terms: returns instances of contact logs that match
    #           the filter).
    def get_context_data(self, **kwargs):
        context = super(PersonDetail, self).get_context_data(**kwargs)
        try:
            context['contact_log'] = contactLog.objects.filter(member=self.kwargs['pk'])
        except ObjectDoesNotExist:
            pass
        return context

class MemberSearchView(HaystackViewSet):
    """
    View that connects the Member search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    index_models = [Person]
    serializer_class = MemberSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]


class FileListCreateView(generics.CreateAPIView):
    """
        View that's responsible for accepting a file and writing it into the database
    """
    queryset = PersonFile.objects.all()
    serializer_class = MemberFileSerializer
    # parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']

        f_name = file_obj.name
        if f_name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
            raise InvalidFile

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
                raise AssertionError('The excel sheet contains invalid fields. '
                                     'Please check the sheet and upload it again')

        for member in json_repr:
            serializer_t = MemberSerializer(data=member)
            serializer_t.is_valid()
            serializer_t.save()

    except AssertionError as e:
        return Response({'Error': str(e)}, status.HTTP_406_NOT_ACCEPTABLE)
    except TypeError as e:
        return Response({'Error': str(e)}, status.HTTP_406_NOT_ACCEPTABLE)
    except ValidationError as e:
        return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    return Response({'Detail': 'Success', 'count': len(json_repr)}, status.HTTP_201_CREATED)

class FileTooLarge(APIException):
    """
        This exceptions gets raised if the file uploaded is exceeding the file size limit
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The file exceeded the file size limit. Please upload a smaller file'
    default_code = 'bad request'


class InvalidFile(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The file is an invalid format. Please supply a valid excel sheet.'
    default_code = 'bad request'




class MemberFilter(filters.FilterSet):
    """
    This is the filter for our members (Person).
    """
    # Declaring our min/max date filters. This allows us to do range searches
    max_bDay = filters.DateFilter(name='bDay', lookup_expr='lte')
    min_bDay = filters.DateFilter(name='bDay', lookup_expr='gte')
    max_hDay = filters.DateFilter(name='hireDate', lookup_expr='lte')
    min_hDay = filters.DateFilter(name='hireDate', lookup_expr='gte')

    class Meta:
        """
        Declaring our model and the fields we want
        """
        model = Person
        # This is a lovely dict of our fields and allowing all on them. This allows
        # =, contains, IN, etc.
        fields = {
            'memberID': '__all__',
            'firstName': '__all__',
            'middleName': '__all__',
            'lastName': '__all__',
            'socNum': '__all__',
            'city': '__all__',
            'mailAddress': '__all__',
            'mailAddress2': '__all__',
            'pCode': '__all__',
            'max_bDay': '__all__',
            'min_bDay': '__all__',
            'gender': '__all__',
            'hPhone': '__all__',
            'cPhone': '__all__',
            'hEmail': '__all__',
            'campus': '__all__',
            'jobType': '__all__',
            'committee': '__all__',
            'membershipStatus': '__all__',
            'max_hDay': '__all__',
            'min_hDay': '__all__',
            'programChoice': '__all__',
        }


#class FilterOffsetClass(LimitOffsetPagination):
    """
    This is our offset. It overwrites what we have in the settings page.
    """
    # default_limit = Person.objects.count()
    # limit_query_param = 'limit'
    # offset_query_param = 'offset'


class MemberFilterView(viewsets.ReadOnlyModelViewSet):
    """
    This is our API for filtering a member. It queries the database for all members and
    filters based on the parameters passed in through the url
    """
    # Defining the queryset to use, serializer, filter class and the fields.
    queryset = Person.objects.all()
    serializer_class = MemberFilterSerializer
    filter_class = MemberFilter
    # filter_fields might not be required but it's better to be safe
    filter_fields = ['id', 'memberID', 'firstName', 'middleName', 'lastName',
                  'socNum', 'city', 'mailAddress', 'mailAddress2', 'pCode',
                  'max_bDay', 'min_bDay', 'gender', 'hPhone', 'cPhone', 'hEmail', 'campus',
                  'jobType', 'committee', 'membershipStatus', 'max_hDay', 'min_hDay', 'programChoice']
    #pagination_class = FilterOffsetClass


class MemberFilterList(TemplateView, FormMixin):
    """
    This is our view that the user will see. It allows the user to make filters requests and view the results.
    """
    template_name = "add_member/member_filter.html"
    form_class = MemberFilterForm


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