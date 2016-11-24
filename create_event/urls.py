from django.conf.urls import url
from . import views

app_name = 'create_event'

urlpatterns = [
    url(r'^$', views.EventCreate.as_view(), name='add_event'),
    url(r'(?P<pk>[-\d]+)', views.EventCreateSuccess.as_view(), name='event_create_success')
]