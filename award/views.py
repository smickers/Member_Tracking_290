from .models import EducationAward
from .forms import EducationAwardForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


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
    
    def get_context_data(self, **kwargs):
        request = self.request
        context = super(EducationAwardDetail, self).get_context_data(**kwargs)
        return context
