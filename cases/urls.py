from django.conf.urls import url
from . import views

app_name = 'cases'

urlpatterns = [

    url(r'list/$', views.CaseList.as_view(), name='case_list'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.CaseUpdate.as_view(), name='case_update'),
    url(r'^(?P<pk>[-\w]+)/$', views.CaseDetail.as_view(), name='case_detail'),
]