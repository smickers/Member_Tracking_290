from django.conf.urls import url
from . import views

app_name = 'meeting'

urlpatterns = [
    # Main creation page url record
    url(r'^$', views.MeetingCreation.as_view(), name='create_meeting'),
    # Success page url record
 url(r'(?P<pk>[-\d]+)', views.MeetingSuccess.as_view(), name='create_meeting_success'),
]