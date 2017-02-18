from django.conf.urls import url
from . import views

app_name = 'contact_log_creation'

urlpatterns = [
    url(r'^add/$', views.ContactLogCreate.as_view(), name='contact_log_add'),
    url(r'^(list)/$', views.ContactLogList.as_view(), name='contact_log_list'),
    url(r'^update/(?P<pk>[-\d]+)$', views.ContactLogEdit.as_view(), name='contact_log_edit'),
    #url(r'^update/(?P<pk>[-\d]+)$', views.contactLogDetail, name='contact_log_edit'),
    # Default case: this regex will match ANYTHING
    url(r'^.*$', views.ContactLogList.as_view(), name='contact_log_list_default'),
]
