from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from add_member.models import Person
from .models import EducationAward
from .models import PDAward
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True

    def setUp(self):
        self.tempPerson = Person()
        self.tempPerson.memberID = 123456789
        self.tempPerson.firstName = 'First'
        self.tempPerson.middleName = 'Middle'
        self.tempPerson.lastName = 'Last'
        self.tempPerson.socNum = 123456789
        self.tempPerson.city = 'Sample City'
        self.tempPerson.mailAddress = 'Sample address'
        self.tempPerson.mailAddress2 = 'Sample Address 2'
        self.tempPerson.hPhone = 3061111234
        self.tempPerson.cPhone = 3061111234
        self.tempPerson.hEmail = 'sample@sample.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Commitee'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '2012-03-03'
        self.tempPerson.pCode = 's7k5j8'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.save()

        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()

        self.pdAward1 = PDAward()
        self.pdAward1.awardName = "Excelence Award"
        self.pdAward1.memberAwarded = self.tempPerson
        self.pdAward1.awardCost = 100
        self.pdAward1.startDate = "2017-02-01"
        self.pdAward1.endDate = "2017-02-01"
        self.pdAward1.full_clean()
        self.pdAward1.save()

    ##PD TESTS

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_pd_award_app(self):
        response = self.client.get(reverse('award:award_pd_list'))
        self.assertContains(response, "List of Professional Development Funding")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('award:award_pd_detail', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_pd_award_app(self):
        response = self.client.get(reverse('award:award_pd_list'))
        self.assertContains(response, "List of Professional Development Funding")
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page_from_pd(self):
        response = self.client.get(reverse('award:award_pd_list'))
        self.assertContains(response, "List of Professional Development Funding")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist_from_pd(self):
        response = self.client.get(reverse('award:award_pd_list'))
        self.assertContains(response, "List of Professional Development Funding")
        response = self.client.get("add_member:member_edit_list")
        self.assertEquals(response.status_code, 404)

    # Education Award Tests

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_edu_award_app(self):
        response = self.client.get(reverse('award:edu_list'))
        self.assertContains(response, "Educational Awards")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('award:award_pd_detail', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside__edu_award_app(self):
        response = self.client.get(reverse('award:edu_list'))
        self.assertContains(response, "Educational Awards")
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page_from_edu(self):
        response = self.client.get(reverse('award:edu_list'))
        self.assertContains(response, "Educational Awards")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist_from_edu(self):
        response = self.client.get(reverse('award:edu_list'))
        self.assertContains(response, "Educational Awards")
        response = self.client.get("add_member:member_edit_list")
        self.assertEquals(response.status_code, 404)
