from django.shortcuts import render
from .models import *
from .forms import GrievanceAwardForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from add_case.models import Case


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
        return { 'case': self.kwargs['pk']}



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
    template_name = 'grievance_award/grievanceaward_list.html'

