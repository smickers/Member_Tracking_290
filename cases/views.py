from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView
from cases.forms import CaseMembersForm
from add_case.models import Case

#view for listing all the members found in the db
class CaseList(ListView):
    model = Case
    template_name = 'cases/cases_list.html'

#view for updating individual member info
class CaseUpdate(UpdateView):
    model = Case
    form_class = CaseMembersForm

#view for displaying individual member info
class CaseDetail(DetailView):
    model = Case
    template_name = 'cases/cases_detail.html'

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(CaseDetail, self).get_context_data(**kwargs)
        print request.POST
        return context


