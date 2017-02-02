from django.shortcuts import render
from .models import EducationAward, PDAward
from .forms import EducationAwardForm, PDAwardForm
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


class PDAwardCreation(CreateView):
    model=PDAward
    form_class = PDAwardForm
    form = PDAwardForm()
    template_name = 'award/pd_award/pd_award_form.html'

class PDAwardDetail(DetailView):
    model = PDAward
    template_name = 'award/pd_award/pd_award_detail.html'