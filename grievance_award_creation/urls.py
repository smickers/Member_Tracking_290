from django.conf.urls import url
from . import views

app_name = 'grievance_award_creation'

urlpatterns = [
    # Main creation page url record
    url(r'^$', views.GrievanceAwardCreation.as_view(), name='create_grievance_award'),
    url(r'(?P<pk>[-\d]+)', views.GrievanceAwardCreationSuccess.as_view(), name='create_grievance_award_success')
    # url(r'cancel/$', views.CancelUpload_view, name='cancel_grievance_upload')

]