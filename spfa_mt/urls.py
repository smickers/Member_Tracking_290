from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact_log/',include('contactLog.urls')),
    #url(r'^contact_log/success/',include('contactLog.urls')),
]
