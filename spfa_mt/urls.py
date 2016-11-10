"""spfa_mt URL Configuration
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addmember/', include('add_member.urls')),
    url(r'^contact_log/',include('contactLog.urls')),
]
