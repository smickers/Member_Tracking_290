from django.shortcuts import render
from .models import *
from .forms import GrievanceAwardForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.files.uploadhandler import StopUpload, SkipFile
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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

    def get_success_url(self):
        return self.object.get_absolute_url()


class GrievanceAwardCreationSuccess(DetailView):
    # Define the model
    model = GrievanceAward


# Class: GrievanceAwardDetail
# Purpose: To display the details of an award
# class GrievanceAwardDetail(DetailView):
#     model = GrievanceAward
#     template_name = 'grievance_award_creation/grievanceaward_actual_detail.html'


    # def get_context_data(self, **kwargs):
    #     context = super(GrievanceAwardDetail, self).get_context_data(**kwargs)
    #     # context["files"] = GrievanceFiles.objects.all().model.file
    #     context["files"] = "hello"
    #     return context

def grievance_award_detail(request, pk):
    gw = GrievanceAward.objects.get(id=pk)
    manager = GrievanceFilesManager()
    gw.files = str(manager.get_files(pk)).split('/')[1]
    return render(request, 'grievance_award_creation/grievanceaward_actual_detail.html', {'object': gw})

# This class declares the form for the editing a grievance award
class GrievanceAwardEditView(UpdateView):
    model = GrievanceAward
    form_class = GrievanceAwardForm

# This class declares the form to show a list of current grievance award
class GrievanceAwardList(ListView):
    model = GrievanceAward
    template_name = 'grievance_award/grievanceaward_list.html'
