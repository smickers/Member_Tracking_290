from django.core.urlresolvers import reverse
from django.test import TestCase, SimpleTestCase, Client
from .models import Case
from add_member.models import Person

# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True
    # variable for our domain
    #domain = 'http://127.0.0.1:8000'

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
        person1.committee = 'Sample Commitee'
        person1.memberImage = 'image.img'
        person1.bDay = '2012-03-03'
        person1.hireDate = '2012-03-03'
        person1.gender = 'MALE'
        person1.membershipStatus = 'RESOURCE'
        person1.programChoice = 'Sample Program'
        person1.full_clean()
        person1.save()
        tempCase = Case()
        tempCase.pk = 1
        tempCase.lead = 123456789
        tempCase.complainant = person1
        # tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
        #                   "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
        #                   "natoque penatibus et magnis dis parturient montes, nascetur " \
        #                   "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
        tempCase.school = "School of Business"
        #tempCase.program = "Architectural Technologies - Diploma"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        #self.client = Client()

    # # Test that we can move from the 'list' page, to the details page for case where PK=3
    # def test_we_can_nav_to_page_within_case_app(self):
    #     response = self.client.get(reverse('add_case:case_list'))
    #     self.assertContains(response, "List of Cases", count=1)
    #     response = self.client.post(reverse('add_case:case_detail', args=('pk', 1)), follow=True)
    #     self.assertRedirects(response, reverse('add_case:case_detail', args=('pk', 1)))
    #
    #
    #     # response = self.client.get('/addCase/list/', follow=True)
    #     # SimpleTestCase.assertRedirects(response, '/addCase/3/', status_code=302, target_status_code=200, msg_prefix='',
    #     #                                fetch_redirect_response=True)

    ####THIS WILL PASS
    def test_we_can_nav_to_page_within_case_app(self):
        response = self.client.get(reverse('add_case:case_list'))
        self.assertContains(response, "List of Cases", count=1)
        #Using post was not allowed, swithing to get returned the web page
        #assertRedirect was looking for response code 302 meaning the page was found
        #using get actully gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('add_case:case_detail', args='1'))
        print response
        self.assertEquals(response.status_code, 200)