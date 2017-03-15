from django.conf.urls import url
from request.router import patterns
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name = 'add_member'

urlpatterns = [
    url(r'add/$', views.PersonCreate.as_view(), name='member_add'),
    url(r'list/$', views.PersonList.as_view(), name='member_list'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.PersonUpdate.as_view(), name='member_update'),
    url(r'^(?P<pk>[-\w]+)/$', views.PersonDetail.as_view(), name='member_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                                  {'document_root': settings.MEDIA_ROOT}))
