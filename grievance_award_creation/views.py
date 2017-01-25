from django.shortcuts import render
from .models import GrievanceAward
from .forms import GrievanceAwardForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
# Class: GrievanceAwardCreation
# Purpose: Links our creation form to a Grievance award to be shown when the user
# wants to create a new award.
class GrievanceAwardCreation(CreateView):
    # Link GrievanceAward to the appropriate grievance award form
    model = GrievanceAward
    form_class = GrievanceAwardForm
    form = GrievanceAwardForm()

# Class: GrievanceAwardCreationSuccess
# Purpose: The view that is shown upon successfully creating a grievance award.
class GrievanceAwardCreationSuccess(DetailView):
    # Define the model
    model = GrievanceAward

    def get_context_data(self, **kwargs):
        context = super(GrievanceAwardCreationSuccess, self).get_context_data(**kwargs)
        return context

# Class: GrievanceAwardDetail
# Purpose: To display the details of an award
class GrievanceAwardDetail(DetailView):
    model = GrievanceAward
    template_name = 'grievance_award_creation/grievanceaward_actual_detail.html'

# This class declares the form for the editing a grievance award
class GrievanceAwardEditView(UpdateView):
    model = GrievanceAward
    form_class = GrievanceAwardForm

# This class declares the form to show a list of current grievance award
class GrievanceAwardList(ListView):
    model = GrievanceAward
    template_name = 'grievance_award/grievanceaward_list.html'
