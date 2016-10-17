from django.conf.urls import url
from . import views

app_name = 'addmember'

urlpatterns=[
    url(r'^$', views.PersonCreate.as_view(), name='member-add'),
]