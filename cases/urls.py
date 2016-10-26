from django.conf.urls import url
from . import views

app_name = 'cases'

urlpatterns = {
    url(r'^$', views.CaseMembersCreate.as_view(), name='addMemberToCase'),
}