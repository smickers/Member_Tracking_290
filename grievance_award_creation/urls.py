from django.conf.urls import url
from . import views, models

app_name = 'grievance_award_creation'

urlpatterns = [
    # Main creation page url record
    url(r'^list/$', views.GrievanceAwardList.as_view(), name='grievance_award_list'),
    url(r'^(?P<pk>[-\d]+)/$', views.GrievanceAwardCreation.as_view(), name='create_grievance_award'),
    # Success page url record
    url(r'^detail/(?P<pk>[-\d]+)$', views.grievance_award_detail, name='grievance_award_actual_detail'),
    url(r'^edit/(?P<pk>[-\d]+)$', views.GrievanceAwardEditView.as_view(), name='grievance_award_edit'),
    url(r'(?P<pk>[-\d]+)', views.GrievanceAwardCreationSuccess.as_view(), name='create_grievance_award_success'),
]