from django.conf.urls import url
from . import views

app_name = 'add_case'

urlpatterns = [
    url(r'^$', views.CaseCreate.as_view(), name='case_add'),
    url(r'^edit/(?P<pk>[-\w]+)$', views.UpdateCaseView.as_view(), name='case_edit'),
    url(r'^list/$', views.CaseList.as_view(), name='case_list'),
    url(r'^(?P<pk>[-\w]+)/$', views.CaseDetail.as_view(), name='case_detail'),
]
