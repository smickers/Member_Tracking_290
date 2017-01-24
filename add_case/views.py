from django.shortcuts import render
from .models import Case
from .forms import CaseForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from drf_haystack.viewsets import HaystackViewSet
from serializer import CaseSearchSerializer
from drf_haystack.filters import HaystackAutocompleteFilter

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
