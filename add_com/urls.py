from django.conf.urls import url
from . import views

app_name = 'add_com'

urlpatterns = [
    url(r'add/$', views.ComCreate.as_view(), name='committee_add'),
    url(r'list/$', views.ComList.as_view(), name='committee_list'),
    url(r'^(?P<pk>[-\w]+)/$', views.ComDetailView.as_view(), name='committee_detail'),
]
