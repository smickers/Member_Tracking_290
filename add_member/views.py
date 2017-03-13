from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person
from .forms import PersonForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer, MemberFilterSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from rest_framework import generics
import django_filters
from rest_framework.response import Response

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


class MemberFilter(django_filters.rest_framework.FilterSet):
    max_bDay = django_filters.DateFilter(name='bDay', lookup_expr='lte')
    min_bDay = django_filters.DateFilter(name='bDay', lookup_expr='gte')
    max_hDay = django_filters.DateFilter(name='hDay', lookup_expr='lte')
    class Meta:
        model = Person
        fields = ['id', 'memberID', 'firstName', 'middleName', 'lastName',
                  'socNum', 'city', 'mailAddress', 'mailAddress2', 'pCode',
                  'max_bDay', 'min_bDay', 'gender', 'hPhone', 'cPhone', 'hEmail', 'campus',
                  'jobType', 'committee', 'membershipStatus', 'hireDate']


class MemberFilterView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = MemberFilterSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = MemberFilter

    # def get(self, request):
    #     response = super(self, request)
    #     return response