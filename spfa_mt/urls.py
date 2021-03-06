""" spfa_mt URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from add_member.views import MemberSearchView, MemberFilterView
from django.conf.urls.static import static
import settings
from add_case.views import CaseSearchView
from add_com.views import CommitteeSearchView
from contact_log.views import ContactLogViewSet, ReportContactLogViewSet
#from contact_log.views import ContactLogSearchView
from grievance_award_creation.views import GrievanceAwardFilterView
from . import views
from wkhtmltopdf.views import PDFTemplateView

# initialize rest framework's router
router = routers.DefaultRouter()

# route the member search functionality to 'member_list/view' url path
router.register('members_list/search', MemberSearchView, base_name='member-search')

# route the case search functionality to 'case_list/view' url
router.register('case_list/search', CaseSearchView, base_name='case-search')

# route the committee search functionality to 'meeting/view' url
router.register('committee_list/search', CommitteeSearchView, base_name='committee-search')

router.register('member/filter', MemberFilterView, base_name='member-filter')
#router.register('contact_log/search', ContactLogSearchView, base_name='contact-log-search')
#router.register(r'contact_log/search', ContactLogViewSet, base_name='contact_log')
router.register('contact_log/search', ContactLogViewSet)
router.register('contact_log/report_search', ReportContactLogViewSet, base_name='report-search')
router.register('grievance_award/filter', GrievanceAwardFilterView)

urlpatterns = [
    url(r'^index.html$', views.spfaView.as_view(), name='index_default'),
    url(r'^$', views.spfaView.as_view(), name='index'),
    # url(r'^$', PDFTemplateView.as_view(template_name='test.html', filename='busta.pdf'), name='index'),
    #rest service's root url
    url(r'^api-root/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^addmember/', include('add_member.urls')),
    url(r'^meeting/', include('meeting.urls')),
    url(r'^addCase/', include('add_case.urls')),
    url(r'^contact_log/', include('contact_log.urls')),
    # url(r'^member/', include('add_member.urls')),
    url(r'^event/', include('create_event.urls')),
    url(r'^award/', include('award.urls')),
    url(r'^grievance/', include('grievance_award_creation.urls')),
    url(r'^add_event/', include('create_event.urls')),
    url(r'^add_com/', include('add_com.urls')),
    url(r'^pdf/', views.PDFView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
