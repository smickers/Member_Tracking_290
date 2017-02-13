from django.conf.urls import url
from . import views, models

app_name = 'grievance_award_creation'

urlpatterns = [
    # Main creation page url record
    url(r'^$', views.GrievanceAwardCreation.as_view(), name='create_grievance_award'),
    # Success page url record
    url(r'^detail/(?P<pk>[-\d]+)$', views.grievance_award_detail, name='grievance_award_actual_detail'),
    url(r'^edit/(?P<pk>[-\d]+)$', views.GrievanceAwardEditView.as_view(), name='grievance_award_edit'),
    url(r'^list/$', views.GrievanceAwardList.as_view(), name='grievance_award_list'),
    url(r'(?P<pk>[-\d]+)', views.GrievanceAwardCreationSuccess.as_view(), name='create_grievance_award_success'),
    url(r'^file/(?P<files>[\w.@\d+-]+)$', views.file_download, name='grievance_file_download')
    # url(r'cancel/$', views.CancelUpload_view, name='cancel_grievance_upload')

]