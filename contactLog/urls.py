from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import altViews

app_name = 'contact_log_creation'

urlpatterns = [
    # Setting up a base URL for creating a contact log
    url(r'^$', views.ContactLogCreate.as_view(), name='contact_log_add'),
    #url(r'/(?P<id>\d+)/^$', views.ContactLogSuccess.as_view(), name='contact_log_success'),
    url(r'(?P<pk>[-\d]+)', views.success, name='success')
]
