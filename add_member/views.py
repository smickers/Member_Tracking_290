from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from .models import Person
from .forms import PersonForm, MemberFilterForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer, MemberFilterSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
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