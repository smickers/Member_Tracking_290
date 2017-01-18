from django.shortcuts import render
from .models import GrievanceAward
from .forms import GrievanceAwardForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

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
#     def post(self, request, *args, **kwargs):
#         form = self.form
#         files = request.FILES.getlist('file_field')
#         return super(GrievanceAwardCreation, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()


class GrievanceAwardCreationSuccess(DetailView):
    # Define the model
    model = GrievanceAward

    # def get_context_data(self, **kwargs):
    #     context = super(GrievanceAwardCreationSuccess, self).get_context_data(**kwargs)
    #     return context
