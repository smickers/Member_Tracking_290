from .models import EducationAward
from .forms import EducationAwardForm
from django.shortcuts import render
from .models import EducationAward, PDAward
from .forms import EducationAwardForm, PDAwardForm, EducationAwardUpdateForm
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

#View shown for updating an educational award
class EduationAwardUpdate(UpdateView):
    model=EducationAward
    form_class = EducationAwardUpdateForm
    template_name = 'award/edu_award/edu_award_form.html'

#View shown for List of Educational Awards
class EduationAwardList(ListView):
    model=EducationAward
    template_name = 'award/edu_award/edu_award_list.html'

#PD AWARD VIEW CLASSES

#Class: PDAwardCreation
#This class is for defining the view for creating a PD Award
class PDAwardCreation(CreateView):
    model=PDAward
    form_class = PDAwardForm
    form = PDAwardForm()
    template_name = 'award/pd_award/pd_award_form.html'

#Class: PDAwardDetail
#This class is for defining the view for a detail page of a PD Award
class PDAwardDetail(DetailView):
    model = PDAward
    template_name = 'award/pd_award/pd_award_detail.html'

# Class: EditPDAwardView
# This class is for defining the view for editing a PD Award
class EditPDAwardView(UpdateView):
    model = PDAward
    form_class = PDAwardForm
    template_name = 'award/pd_award/pd_award_form.html'

# Class: PDAwardList
# This class is for defining the view for the list of all PD Awards
class PDAwardList(ListView):
    model = PDAward
    template_name = 'award/pd_award/pd_award_list.html'
