from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'contact_log_creation'

urlpatterns = [
    # Setting up a base URL for creating a contact log
    url(r'^$', views.ContactLogCreate.as_view(), name='contact_log_add'),
    #url(r'^$', views.ContactLogSuccess.as_view(), name='contact_log_success')
]
