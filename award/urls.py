from django.conf.urls import url
from . import views

app_name = 'award'
# NOTE FOR UPKEEP:
# When adding awards, please make sure that you leave a comment before your new URLs.
# As well, ensure that you have an appropriate abbreviation in your regex: for example, education awards redirect to
#   '/edu/' and then whatever the specific regex is.
urlpatterns = [
    # Education Awards:
    url(r'edu/create/$', views.EducationAwardCreate.as_view(), name='edu_create'),
    url(r'^(?P<pk>[-\w]+)$', views.EducationAwardDetail.as_view(), name='edu_detail'),

    # Professional Development Awards
    url(r'pd/create/$', views.PDAwardCreation.as_view(), name='award_pd_create'),
    # Edit page url record
    url(r'^pd/edit/(?P<pk>[-\d]+)/$', views.EditPDAwardView.as_view(), name='award_pd_edit'),
    # List page url record
    url(r'^pd/list/$', views.PDAwardList.as_view(), name='award_pd_list'),
    # PD Award Detail view
    url(r'^/pd/detail/(?P<pk>[-\w]+)/$', views.PDAwardDetail.as_view(), name='award_pd_detail'),
]
