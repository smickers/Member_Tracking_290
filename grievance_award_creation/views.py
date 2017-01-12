from django.shortcuts import render
from .models import GrievanceAward
from .forms import GrievanceAwardForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.forms.models import inlineformset_factory
from .models import GrievanceFiles
# Create your views here.
class GrievanceAwardCreation(CreateView):
    model = GrievanceAward
    form_class = GrievanceAwardForm
    form = GrievanceAwardForm()

    def post(self, request, *args, **kwargs):
        form = self.form
        files = request.FILES.getlist('file_field')
        return super(GrievanceAwardCreation, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()


class GrievanceAwardCreationSuccess(DetailView):
    model = GrievanceAward

    def get_context_data(self, **kwargs):
        context = super(GrievanceAwardCreationSuccess, self).get_context_data(**kwargs)
        return context
