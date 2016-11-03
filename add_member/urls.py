from django.conf.urls import url
from . import views

app_name = 'add_member'

urlpatterns = [
    url(r'add/$', views.PersonCreate.as_view(), name='member_add'),
    url(r'list/$', views.PersonList.as_view(), name='member_list'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.PersonUpdate.as_view(), name='member_update'),
    url(r'^(?P<pk>[-\w]+)/$', views.PersonDetail.as_view(), name='member_detail'),

]