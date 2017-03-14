from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from .models import Person
from .forms import PersonForm, MemberFilterForm
from drf_haystack.viewsets import HaystackViewSet
from .serializer import MemberSearchSerializer, MemberFilterSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from rest_framework import generics, viewsets
import rest_framework_filters as filters


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


class MemberFilter(filters.FilterSet):
    """
    This is the filter for our members (Person).
    """
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
        # = or contains, etc.
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
        }


class MemberFilterView(viewsets.ReadOnlyModelViewSet):
    """
    This is our API for filtering a member. It queries the database for all members and
    filters based on the parameters passed in through the url
    """
    queryset = Person.objects.all()
    serializer_class = MemberFilterSerializer
    filter_class = MemberFilter
    filter_fields = ['id', 'memberID', 'firstName', 'middleName', 'lastName',
                  'socNum', 'city', 'mailAddress', 'mailAddress2', 'pCode',
                  'max_bDay', 'min_bDay', 'gender', 'hPhone', 'cPhone', 'hEmail', 'campus',
                  'jobType', 'committee', 'membershipStatus', 'hireDate']


class MemberFilterList(TemplateView, FormMixin):
    template_name = "add_member/member_filter.html"
    form_class = MemberFilterForm
