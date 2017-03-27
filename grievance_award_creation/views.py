from django.shortcuts import render
from .models import *
from .forms import GrievanceAwardForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from add_case.models import Case
from .serializer import GAFilterSerializer
from rest_framework import viewsets
import rest_framework_filters as filters
from rest_framework.pagination import LimitOffsetPagination
from django.core.validators import EMPTY_VALUES


# Create your views here.
# Class: GrievanceAwardCreation
# Purpose: Links our creation form to a Grievance award to be shown when the user
# wants to create a new award.
class GrievanceAwardCreation(CreateView):
    # Link GrievanceAward to the appropriate grievance award form
    model = GrievanceAward
    form_class = GrievanceAwardForm
    context_object_name = "grievance_award"

    def get_context_data(self, **kwargs):
        context = super(GrievanceAwardCreation, self).get_context_data(**kwargs)
        context['case'] = Case.objects.get(pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        return {'case': self.kwargs['pk']}


class GrievanceAwardCreationSuccess(DetailView):
    # Define the model
    model = GrievanceAward


# Function: grievance_award_detail
# Purpose: function based view for viewing the details of a grievance award and its files
def grievance_award_detail(request, pk):
    gw = GrievanceAward.objects.get(id=pk)
    manager = GrievanceFilesManager()
    try:
        file = manager.get_files(pk)
        gw.file_name = str(file).split('/')[1]
        gw.file_desc = file.description
        gw.file_date_uploaded = file.date_uploaded
    # if the grievance award has no files associated, empty the fields and dont display the html
    except:
        gw.file_name = ""
        gw.file_desc = ""
        gw.file_date_uploaded = ""

    return render(request, 'grievance_award_creation/grievanceaward_actual_detail.html', {'grievance_award': gw})


# This class declares the form for the editing a grievance award
class GrievanceAwardEditView(UpdateView):
    model = GrievanceAward
    form_class = GrievanceAwardForm


# This class declares the form to show a list of current grievance award
class GrievanceAwardList(ListView):
    model = GrievanceAward
    template_name = 'grievance_award_creation/grievanceaward_list.html'


class EmptyStringFilter(filters.BooleanFilter):
    """
    Writing a custom filter so we can get all results with empty strings.
    """
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.name: ""})


class GrievanceAwardFilter(filters.FilterSet):
    """
    This is the filter for our Grievance Award.
    """
    # Declaring our min/max date filters. This allows us to do range searches
    min_date = filters.DateFilter(name='date', lookup_expr='gte')
    max_date = filters.DateFilter(name='date', lookup_expr='lte')
    min_amount = filters.NumberFilter(name='awardAmount', lookup_expr='gte')
    max_amount = filters.NumberFilter(name='awardAmount', lookup_expr='lte')
    policy = filters.NumberFilter(name='case__caseType', lookup_expr='lte')
    empty_desc_filter = EmptyStringFilter(name='description')

    class Meta:
        """
        Declaring our model and the fields we want
        """
        model = GrievanceAward

        # This is a lovely dict of our fields and allowing all on them. This allows
        # =, contains, IN, etc.
        fields = {
            # 'grievanceType': '__all__',
            'awardAmount': '__all__',
            'description': '__all__',
            'date': '__all__',
            'case__caseType': '__all__'
        }


class FilterOffsetClass(LimitOffsetPagination):
    """
    This is our offset. It overwrites what we have in the settings page.
    """
    try:
        default_limit = GrievanceAward.objects.count()
        limit_query_param = 'limit'
        offset_query_param = 'offset'
    except Exception as e:
        pass


class GrievanceAwardFilterView(viewsets.ReadOnlyModelViewSet):
    """
    This is our API for filtering a Grievance Award. It queries the database for all Grievance Award and
    filters based on the parameters passed in through the url
    """
    # Defining the queryset to use, serializer, filter class and the fields.
    queryset = GrievanceAward.objects.all()
    # def get_queryset(self):
    #     if 'empty_desc_filter' in self.request.QUERY_PARAMS:
    #         return self.model.objects.filter(description="")
    #     return self.model.objects.all()
    serializer_class = GAFilterSerializer
    filter_class = GrievanceAwardFilter
    # filter_fields might not be required but it's better to be safe
    filter_fields = [
        'awardAmount', 'description', 'date'
    ]
    pagination_class = FilterOffsetClass
