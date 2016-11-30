#spfa_mt URL Configuration
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addmember/', include('add_member.urls')),
    url(r'^cases/', include('cases.urls')),
    url(r'^addCase/', include('add_case.urls')),
    url(r'^contact_log/', include('contactLog.urls')),
    url(r'^member/', include('add_member.urls')),
]
