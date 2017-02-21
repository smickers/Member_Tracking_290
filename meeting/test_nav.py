from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from .models import Meeting
from add_com.models import Committee
from add_member.models import Person


# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True
    committee = Committee()
    person1 = Person()

    # #setup
    def setUp(self):
        self.committee.name = "Finance"
        self.committee.status = 1
        self.committee.full_clean()
        self.committee.save()

        self.person1.memberID = 4204444
        self.person1.firstName = 'Larry'
        self.person1.middleName = 'Marco'
        self.person1.lastName = 'Leisureman'
        self.person1.socNum = 123456789
        self.person1.city = 'Maple Ridge'
        self.person1.mailAddress = '123 Fake St'
        self.person1.mailAddress2 = 'Sample Address 2'
        self.person1.pCode = 's7k5j8'
        self.person1.hPhone = '(306)812-1234'
        self.person1.cPhone = '(306)812-1234'
        self.person1.hEmail = 'sample@sample.com'
        self.person1.campus = 'SASKATOON'
        self.person1.jobType = 'FTO'
        self.person1.committee = 'Sample Committee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_meeting_app(self):
        response = self.client.get(reverse('meeting:meeting_list'))
        self.assertContains(response, "List of Meetings")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('meeting:create_meeting_success', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_case_app(self):
        response = self.client.get(reverse('meeting:meeting_list'))
        self.assertContains(response, "List of Meetings")
        response = self.client.get(reverse('add_member:member_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page(self):
        response = self.client.get(reverse('meeting:meeting_list'))
        self.assertContains(response, "List of Meetings")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist(self):
        response = self.client.get(reverse('meeting:meeting_list'))
        self.assertContains(response, "List of Meetings")
        response = self.client.get("meeting:,meeting_edit_list")
        self.assertEquals(response.status_code, 404)
