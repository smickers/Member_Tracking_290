from django.shortcuts import render
from .models import EducationAward
from .forms import EducationAwardForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
###
# Views for Education Awards
###


# View shown upon navigating to the "create education award" page:
class EducationAwardCreation(CreateView):
    model = EducationAward
    form_class = EducationAwardForm
    form = EducationAwardForm()
    template_name = 'award/edu_award/edu_award_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


# View shown upon successfully creating an education award:
class EducationAwardCreationSuccess(DetailView):
    # Define the model
    model = EducationAward
    template_name = 'award/edu_award/edu_award_form.html'

    def get_context_data(self, **kwargs):
        context = super(EducationAwardCreationSuccess, self).get_context_data(**kwargs)
        return context


# View shown regarding details on a specific education award:
class EducationAwardDetail(DetailView):
    model = EducationAward
    template_name = 'award/edu_award/edu_award_detail.html'
