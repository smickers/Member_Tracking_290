from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'contact_log_creation'

urlpatterns = [
    # Setting up a base URL for creating a contact log
    url(r'^$', views.ContactLogCreate.as_view(), name='contact_log_add'),
    # A URL entry to redirect the user after submitting a contact log
    url(r'(?P<pk>[-\d]+)', views.success, name='success')
]
