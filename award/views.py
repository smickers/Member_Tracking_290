from .models import EducationAward
from .forms import EducationAwardForm
from django.shortcuts import render
from .models import EducationAward, PDAward
from .forms import EducationAwardForm, PDAwardForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


###
# Views for Education Awards
###
# View shown upon navigating to the "create education award" page:
class EducationAwardCreate(CreateView):
    model = EducationAward
    form_class = EducationAwardForm
    form = EducationAwardForm()
    template_name = 'award/edu_award/edu_award_form.html'


# View shown regarding details on a specific education award:
class EducationAwardDetail(DetailView):
    model = EducationAward
    template_name = 'award/edu_award/edu_award_detail.html'



#PD AWARDS

class PDAwardCreation(CreateView):
    model=PDAward
    form_class = PDAwardForm
    form = PDAwardForm()
    template_name = 'award/pd_award/pd_award_form.html'

class PDAwardDetail(DetailView):
    model = PDAward
    template_name = 'award/pd_award/pd_award_detail.html'

# Class: MeetingEditView
# This class declares the form for the editing a meeting
class EditPDAwardView(UpdateView):
    model = PDAward
    form_class = PDAwardForm
    template_name = 'award/pd_award/pd_award_form.html'

# Class: MeetingList
# This class declares the form to show a list of current meetings
class PDAwardList(ListView):
    model = PDAward
    template_name = 'award/pd_award/pd_award_list.html'
