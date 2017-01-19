from django.shortcuts import render
from .models import GrievanceAward
from .forms import GrievanceAwardForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.files.uploadhandler import StopUpload, SkipFile
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
# Class: GrievanceAwardCreation
# Purpose: Links our creation form to a Grievance award to be shown when the user
# wants to create a new award.
class GrievanceAwardCreation(CreateView):
    # Link GrievanceAward to the appropriate grievance award form
    model = GrievanceAward
    form_class = GrievanceAwardForm
    # form = GrievanceAwardForm()



# Class: GrievanceAwardCreationSuccess
# Purpose: The view that is shown upon successfully creating a grievance award.

    def get_success_url(self):
        return self.object.get_absolute_url()


class GrievanceAwardCreationSuccess(DetailView):
    # Define the model
    model = GrievanceAward

    # def get_context_data(self, **kwargs):
    #     context = super(GrievanceAwardCreationSuccess, self).get_context_data(**kwargs)
    #     return context

# @csrf_exempt
# def CancelUpload_view(request):
#     try:
#         request.upload_handlers=[ CancelUpload(request)]
#     except:
#         return JsonResponse({'cancelled': 'false'})
#     return _CancelUpload_view(request)
#
# @csrf_protect
# def _CancelUpload_view(request):
#     return JsonResponse({'cancelled': 'true'})
#
#
