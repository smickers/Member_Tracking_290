from django.conf.urls import url
from . import views

app_name = 'add_com'

urlpatterns = [
    url(r'add/$', views.ComCreate.as_view(), name='com_add'),
    url(r'list/$', views.ComList.as_view(), name='com_list')
]
