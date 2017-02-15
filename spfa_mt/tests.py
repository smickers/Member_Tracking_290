from django.test import SimpleTestCase
from bs4 import BeautifulSoup
from django.test import Client
from django.core.urlresolvers import reverse
from add_member.models import Person
from add_case.models import Case
from add_com.models import Committee
from award.models import PDAward, EducationAward
from contact_log.models import contactLog
from create_event.models import Event
from grievance_award_creation.models import GrievanceAward
from meeting.models import Meeting
from spfa_mt.urls import urlpatterns


# Test for navigation bar element in entire SPFA-MT application
class TestAllSPFAMTElements(SimpleTestCase):
    # Set this to True so SimpleTestCase can query our DB
    allow_database_queries = True

    # Giant setup method that creates, essentially, everything in the entire application.
    def setUp(self):
        person1 = Person()
        person1.memberID = 4204444
        person1.firstName = 'First'
        person1.middleName = 'Middle'
        person1.lastName = 'Last'
        person1.socNum = 123456789
        person1.city = 'Sample City'
        person1.mailAddress = 'Sample address'
        person1.mailAddress2 = 'Sample Address 2'
        person1.pCode = 's7k5j8'
        person1.hPhone = '(306)812-1234'
        person1.cPhone = '(306)812-1234'
        person1.hEmail = 'sample@sample.com'
        person1.campus = 'SASKATOON'
        person1.jobType = 'FTO'
        person1.committee = 'Sample Committee'
        person1.memberImage = 'image.img'
        person1.bDay = '2012-03-03'
        person1.hireDate = '2012-03-03'
        person1.gender = 'MALE'
        person1.membershipStatus = 'RESOURCE'
        person1.programChoice = 'Sample Program'
        person1.full_clean()
        person1.save()
        temp_case = Case()
        temp_case.pk = 1
        temp_case.lead = 123456789
        temp_case.complainant = person1
        temp_case.school = "School of Business"
        temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        temp_case.status = "OPEN"
        temp_case.docs = None
        temp_case.logs = None
        temp_case.date = "2016-10-20"
        temp_case.save()
        testCom = Committee()
        testCom.name = "Test Committee"
        testCom.status = 1
        testCom.full_clean()
        testCom.save()
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()
        pdAward1 = PDAward()
        pdAward1.awardName = "Excellence Award"
        pdAward1.memberAwarded = person1
        pdAward1.awardCost = 100
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()
        tempCLog = contactLog()
        tempCLog.member = person1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        tempCLog.save()
        testEvent = Event()
        testEvent.name = "Fun Event"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()
        ga = GrievanceAward()
        ga.grievanceType = "M"
        ga.recipient = person1
        ga.case = temp_case
        ga.awardAmount = 500.00
        ga.description = ""
        ga.date = '2016-12-01'
        ga.full_clean()
        ga.save()
        testMeeting = Meeting()
        testMeeting.committee = testCom
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(person1)
        testMeeting.save()

    # Test that the navigation bar menu exists on index.html
    def test_nav_bar_exists_on_main_page(self):
        client = Client()
        source_code = client.get(reverse('index_default'))
        soup = BeautifulSoup(source_code.content, "html.parser")
        soup.prettify()
        self.assertTrue(soup.find("nav"))

    # Test that the footer exists on index.html
    def test_footer_exists_on_main_pages(self):
        client = Client()
        source_code = client.get(reverse('index_default'))
        soup = BeautifulSoup(source_code.content, "html.parser")
        soup.prettify()
        self.assertTrue(soup.find("div", attrs={"class": "footer"}))

    # Test that the header image exists on index.html
    def test_header_image_on_main_page(self):
        client = Client()
        source_code = client.get(reverse('index_default'))
        soup = BeautifulSoup(source_code.content, "html.parser")
        soup.prettify()
        self.assertTrue(soup.find("img"))

    def test_navigation_exists_in_add_and_list_pages(self):
        client = Client()
        # I hard-coded this and I HATE THAT, I tried to find an easier/cleaner/DRY-er option and couldn't
        # Ideally you could include the urlpatterns from spfa_mt, and then for each url listed, go through each of
        # THOSE, and THEN do the check.
        test_patterns = ["add_member:member_add", "add_member:member_list", "add_case:case_add", "add_case:case_list",
                         "add_com:committee_add", "add_com:committee_list", "award:edu_create","award:edu_list",
                         "award:award_pd_create", "award:award_pd_list", "contact_log_creation:contact_log_add",
                         "contact_log_creation:contact_log_list_default", "create_event:add_event",
                         "create_event:list_event", "grievance_award_creation:create_grievance_award",
                         "grievance_award_creation:grievance_award_list", "meeting:create_meeting",
                         "meeting:meeting_list", "add_member:member_detail", "add_case:case_detail",
                         "add_com:committee_detail", "award:edu_detail", "award:award_pd_detail",
                         "create_event:event_detail", "grievance_award_creation:create_grievance_award_success",
                         "meeting:meeting_detail"]
        for app in test_patterns:
            if app.__contains__("detail") or app.__contains__("success"):
                src = client.get(reverse(app, args='1'))
            else:
                src = client.get(reverse(app))
            soup = BeautifulSoup(src.content, "html.parser")
            soup.prettify()
            self.assertTrue(soup.find("nav"))
            self.assertTrue(soup.find("div", attrs={"class": "footer"}))
            self.assertTrue(soup.find("img"))