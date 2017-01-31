from django.conf.urls import url
from . import views

app_name = 'meeting'

urlpatterns = [
    # Main creation page url record
    url(r'^$', views.MeetingCreation.as_view(), name='create_meeting'),
    # Detail page url record
    url(r'^detail/(?P<pk>[-\d]+)$', views.MeetingDetail.as_view(), name='meeting_detail'),
    # Edit page url record
    url(r'^edit/(?P<pk>[-\d]+)$', views.MeetingEditView.as_view(), name='meeting_edit'),
    # List page url record
    url(r'^list/$', views.MeetingList.as_view(), name='meeting_list'),
    # Success page url record
    url(r'(?P<pk>[-\d]+)', views.MeetingSuccess.as_view(), name='create_meeting_success')

]
