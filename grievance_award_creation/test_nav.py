from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from .models import GrievanceAward
from add_member.models import Person
from add_case.models import Case, CasePrograms



# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True
    tempPerson = Person()
    person_pk = -1
    tempCase = Case()
    case_pk = -1
    program = CasePrograms()
    ga = GrievanceAward()

    # setup
    def setUp(self):
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

        self.tempPerson.memberID = 1
        self.tempPerson.firstName = 'First'
        self.tempPerson.middleName = 'Middle'
        self.tempPerson.lastName = 'Last'
        self.tempPerson.socNum = 123456789
        self.tempPerson.city = 'Sample City'
        self.tempPerson.mailAddress = 'Sample address'
        self.tempPerson.mailAddress2 = 'Sample Address 2'
        self.tempPerson.pCode = 's7k5j8'
        self.tempPerson.hPhone = '(306)812-1234'
        self.tempPerson.cPhone = '(306)812-1234'
        self.tempPerson.hEmail = 'sample@sample.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Commitee'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '2012-03-03'
        self.tempPerson.hireDate = '2012-03-03'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.membershipStatus = 'RESOURCE'
        self.tempPerson.programChoice = 'Sample Program'
        self.tempPerson.full_clean()
        self.tempPerson.save()

        self.person_pk = Person.objects.get(memberID=1).pk

        self.tempCase = Case()
        self.tempCase.lead = self.tempPerson.id
        self.tempCase.complainant = self.tempPerson
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.program = self.program
        self.tempCase.caseType = 3
        self.tempCase.status = "OPEN"
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()


        self.ga.case = self.tempCase
        self.ga.awardAmount = 500.00
        self.ga.description = ""
        self.ga.date = '2016-12-01'
        self.ga.full_clean()
        self.ga.save()

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_meeting_app(self):
        response = self.client.get(reverse('grievance_award_creation:grievance_award_list'))
        self.assertContains(response, "List of Grievance Awards")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('grievance_award_creation:grievance_award_actual_detail', args=[self.ga.pk]))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_case_app(self):
        response = self.client.get(reverse('grievance_award_creation:grievance_award_list'))
        self.assertContains(response, "List of Grievance Awards")
        response = self.client.get(reverse('add_member:member_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page(self):
        response = self.client.get(reverse('grievance_award_creation:grievance_award_list'))
        self.assertContains(response, "List of Grievance Awards")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist(self):
        response = self.client.get(reverse('grievance_award_creation:grievance_award_list'))
        self.assertContains(response, "List of Grievance Awards")
        response = self.client.get("grievance_award_creation:,grievance_award_edit_list")
        self.assertEquals(response.status_code, 404)
