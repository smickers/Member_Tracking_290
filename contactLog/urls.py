from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'contact_log_creation'

urlpatterns = [
    url(r'^$', views.ContactLogCreate.as_view(), name='contact_log_add')
]
