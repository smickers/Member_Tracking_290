from django.shortcuts import render
from .models import Case
from .forms import CaseForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from drf_haystack.viewsets import HaystackViewSet
from serializer import CaseSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter
from django.core.exceptions import ValidationError


class CaseCreate(CreateView):
    model = Case
    form_class = CaseForm

class CaseSearchView(HaystackViewSet):
    """
    View that connects the Member search serializer.
    This view will then be used by restframework for routing into a browsable url
    """
    index_models = [Case]
    serializer_class = CaseSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]
    """
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
        """
