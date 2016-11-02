from django.conf.urls import url
from . import views

app_name = 'add_member'

urlpatterns = [
    url(r'add', views.PersonCreate.as_view(), name='member_add'),
    url(r'list', views.PersonEdit.as_view(), name='member_update'),
]