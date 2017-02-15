from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from .models import Case
from add_member.models import Person


# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True

    # #setup
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
        temp_case.caseType = 3
        temp_case.status = "OPEN"
        temp_case.docs = None
        temp_case.logs = None
        temp_case.date = "2016-10-20"
        temp_case.save()

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_case_app(self):
        response = self.client.get(reverse('add_case:case_list'))
        self.assertContains(response, "List of Cases")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('add_case:case_detail', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_case_app(self):
        response = self.client.get(reverse('add_case:case_list'))
        self.assertContains(response, "List of Cases")
        response = self.client.get(reverse('add_member:member_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page(self):
        response = self.client.get(reverse('add_case:case_list'))
        self.assertContains(response, "List of Cases")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist(self):
        response = self.client.get(reverse('add_case:case_list'))
        self.assertContains(response, "List of Cases")
        response = self.client.get("add_case:case_edit_list")
        self.assertEquals(response.status_code, 404)
