""" spfa_mt URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from add_member.views import MemberSearchView
from django.conf.urls.static import static
import settings
from add_case.views import CaseSearchView
from add_com.views import CommitteeSearchView
from . import views

# initialize rest framework's router
router = routers.DefaultRouter()

# route the member search functionality to 'member_list/view' url path
router.register('members_list/search', MemberSearchView, base_name='member-search')

# route the case search functionality to 'case_list/view' url
router.register('case_list/search', CaseSearchView, base_name='case-search')

# route the committee search functionality to 'meeting/view' url
router.register('committee_list/search', CommitteeSearchView, base_name='committee-search')


urlpatterns = [
    url(r'^index.html$', views.spfaView.as_view(), name='index_default'),
    url(r'^$', views.spfaView.as_view(), name='index'),
    #rest service's root url
    url(r'^api-root/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^addmember/', include('add_member.urls')),
    url(r'^meeting/', include('meeting.urls')),
    url(r'^addCase/', include('add_case.urls')),
    url(r'^contact_log/', include('contact_log.urls')),
    url(r'^member/', include('add_member.urls')),
    url(r'^event/', include('create_event.urls')),
    url(r'^award/', include('award.urls')),
    url(r'^grievance/', include('grievance_award_creation.urls')),
    url(r'^add_event/', include('create_event.urls')),
    url(r'^add_com/', include('add_com.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
