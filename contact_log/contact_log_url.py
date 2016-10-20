from django.conf.urls import url
from . import contact_log_view

urlpatterns = [
    url(r'^.*$',contact_log_view.index, name='index'),
]
