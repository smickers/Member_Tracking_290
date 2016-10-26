from django.conf.urls import url
from . import views

app_name = 'add_member'

urlpatterns = [
    url(r'^$', views.PersonCreate.as_view(), name='member_add'),
]