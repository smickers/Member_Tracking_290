from django.shortcuts import render
from .models import Case
from .forms import CaseForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError


class CaseCreate(CreateView):
    model = Case
    form_class = CaseForm

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(CaseCreate, self).get_context_data(**kwargs)
        print "POST REQUEST:"
        print request.POST
        #  print request.META.HTTP_ACCEPT
        if request.POST:
            for mem in request['additionalMembers']:
                if mem == request['complainant']:
                    raise ValidationError("C/N cannot be AM.")
        # print request.GET
        return context
