from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'add_member'

urlpatterns = [
    url(r'add/$', views.PersonCreate.as_view(), name='member_add'),
    url(r'list/$', views.PersonList.as_view(), name='member_list'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.PersonUpdate.as_view(), name='member_update'),
    url(r'^(?P<pk>[-\w]+)/$', views.PersonDetail.as_view(), name='member_detail'),
    #url(r'^media/(?P<path>.*)$', views.static.serve.as_view(),{'document_root': settings.MEDIA_ROOT}),
    url(r'^download/(?P<file_name>.+)$', views.download, name='member_file_download')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#      urlpatterns += ('', (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                                  {'document_root': settings.MEDIA_ROOT}))
