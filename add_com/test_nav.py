from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from models import Committee
from add_member.models import Person
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True
    testCom = Committee()

    def setUp(self):
        self.testCom.name = "Test Committee"
        self.testCom.status = 1
        self.testCom.full_clean()
        self.testCom.save()

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_committee_app(self):
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertContains(response, "List of Committees")
        # Using post was not allowed, switching to using get returned the web page
        # assertRedirect was looking for response code 302 meaning the page was found
        # using get actually gets the page and will tell you if it exists returning response code 200
        # so compare response code to 200 to make sure it went to the page
        response = self.client.get(reverse('add_com:committee_detail', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_committee_app(self):
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertContains(response, "List of Committees")
        response = self.client.get(reverse('add_member:member_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page(self):
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertContains(response, "List of Committees")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist(self):
        response = self.client.get(reverse('add_com:committee_list'))
        self.assertContains(response, "List of Committees")
        response = self.client.get("add_com:committee_edit_list")
        self.assertEquals(response.status_code, 404)
