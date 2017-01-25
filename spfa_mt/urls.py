"""spfa_mt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from add_member.views import MemberSearchView
from add_case.views import CaseSearchView

#initialize rest framework's router
router = routers.DefaultRouter()

#route the member search functionality to 'member_list/view' url path
router.register('members_list/search', MemberSearchView, base_name='member-search')

#route the case search functionality to 'case_list/view' url
router.register('case_list/search', CaseSearchView, base_name='case-search')


urlpatterns = [
    #rest service's root url
    url(r'^api-root/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^addmember/', include('add_member.urls')),
    url(r'^cases/', include('cases.urls')),
    url(r'^addCase/', include('add_case.urls')),
    url(r'^contact_log/', include('contactLog.urls')),
    url(r'^member/', include('add_member.urls')),
    url(r'^event/', include('create_event.urls')),
    #url(r'^add_event/', include('create_event.urls')),
    url(r'^grievance/', include('grievance_award_creation.urls')),
    url(r'^add_event/', include('create_event.urls')),
    url(r'^add_com/', include('add_com.urls'))
]
