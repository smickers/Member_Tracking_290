from django.conf.urls import url
from . import views

app_name = 'create_event'

urlpatterns = [
    url(r'^$', views.EventCreate.as_view(), name='add_event'),  # main event creation page
    url(r'^list/$', views.EventList.as_view(), name='list_event'),
    url(r'^detail/(?P<pk>[-\d]+)$', views.EventDetailView.as_view(), name='event_detail'),
    url(r'^add_member/(?P<pk>[-\d]+)$', views.EventAddMember.as_view(), name='event_add_member'),
    url(r'^edit_member/(?P<pk>[-\d]+)$', views.EventEditView.as_view(), name='event_edit_member'),
    url(r'(?P<pk>[-\d]+)', views.EventCreateSuccess.as_view(), name='event_create_success')   # success page for event

]