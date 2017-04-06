from django.conf.urls import url, include
from . import views
from rest_framework import routers

app_name = 'contact_log_creation'

# router = routers.DefaultRouter()
# router.register(r'contact_log', views.ContactLogViewSet)

urlpatterns = [
    #url(r'^api/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^add/$', views.ContactLogCreate.as_view(), name='contact_log_add'), 
    # Add a new contact log, and pass in a member's PK (same as edit essentially, but we don't want that URL)
    url(r'^add_direct/mid=(?P<pk>[-\d]+)$', views.ContactLogCreate.as_view(), name='contact_log_add_direct'),
    url(r'^(list)/$', views.ContactLogList.as_view(), name='contact_log_list'),
    url(r'^update/(?P<pk>[-\d]+)$', views.ContactLogEdit.as_view(), name='contact_log_edit'),
    url(r'^details/(?P<pk>[-\d]+)$', views.ContactLogDetails.as_view(), name='details'),
    #url(r'^update/(?P<pk>[-\d]+)$', views.contactLogDetail, name='contact_log_edit'),
    # Default case: this regex will match ANYTHING
    url(r'^.*$', views.ContactLogList.as_view(), name='contact_log_list_default'),
]
