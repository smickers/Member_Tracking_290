from django.conf.urls import url
from . import views

app_name = 'add_case'

urlpatterns = [
    url(r'^$', views.CaseCreate.as_view(), name='case_add'),
]
