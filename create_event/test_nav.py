from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from .models import Event
from add_member.models import Person
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class for testing the HTML navbar navigation within this app, and between this app and others.
class TestNav(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True
    testEvent = None
    tempPerson = None
    tempPerson2 = None
    not_saved_person = None

    # setup
    def setUp(self):
        self.testEvent = Event()
        self.testEvent.name = "Fun Event"
        self.testEvent.description = ""
        self.testEvent.date = "2016-12-25"
        self.testEvent.location = "Saskatoon"
        self.testEvent.full_clean()
        self.testEvent.save()

        self.tempPerson = Person()
        self.tempPerson.memberID = 123456789
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

        self.tempPerson2 = Person()
        self.tempPerson2.memberID = 123456789
        self.tempPerson2.firstName = 'First'
        self.tempPerson2.middleName = 'Middle'
        self.tempPerson2.lastName = 'Last'
        self.tempPerson2.socNum = 123456789
        self.tempPerson2.city = 'Sample City'
        self.tempPerson2.mailAddress = 'Sample address'
        self.tempPerson2.mailAddress2 = 'Sample Address 2'
        self.tempPerson2.pCode = 's7k5j8'
        self.tempPerson2.hPhone = '(306)812-1234'
        self.tempPerson2.cPhone = '(306)812-1234'
        self.tempPerson2.hEmail = 'sample@sample.com'
        self.tempPerson2.campus = 'SASKATOON'
        self.tempPerson2.jobType = 'FTO'
        self.tempPerson2.committee = 'Sample Commitee'
        self.tempPerson2.memberImage = 'image.img'
        self.tempPerson2.bDay = '2012-03-03'
        self.tempPerson2.hireDate = '2012-03-03'
        self.tempPerson2.gender = 'MALE'
        self.tempPerson2.membershipStatus = 'RESOURCE'
        self.tempPerson2.programChoice = 'Sample Program'
        self.tempPerson2.full_clean()
        self.tempPerson2.save()

    # Test to show we can move from one page to another within an app
    def test_we_can_nav_to_page_within_meeting_app(self):
        response = self.client.get(reverse('create_event:list_event'))
        self.assertContains(response, "List of Events")
        response = self.client.get(reverse('create_event:event_detail', args='1'))
        self.assertEquals(response.status_code, 200)

    # Test to show we can move from one page to another page in a different app
    def test_we_can_navigate_to_a_page_outside_case_app(self):
        response = self.client.get(reverse('create_event:list_event'))
        self.assertContains(response, "List of Events")
        response = self.client.get(reverse('add_member:member_list'))
        self.assertEquals(response.status_code, 200)

    # Test to show that we can get to a landing page from any other pages
    def test_we_can_navigate_to_a_landing_page(self):
        response = self.client.get(reverse('create_event:list_event'))
        self.assertContains(response, "List of Events")
        response = self.client.get("http://127.0.0.1:8000")
        self.assertEquals(response.status_code, 200)

    # Test to prove that e cannot navigate to a page that doesn't exist
    def test_we_cannot_navigate_to_a_page_that_doesnt_exist(self):
        response = self.client.get(reverse('create_event:list_event'))
        self.assertContains(response, "List of Events")
        response = self.client.get("create_event: event_edit_list")
        self.assertEquals(response.status_code, 404)

    # Test that the navigation bar menu exists on all pages in the Case app
    def test_nav_bar_exists_on_all_case_pages(self):
        with self.assertEquals(self, True):
            # Only test that uses Selenium
            ch = webdriver.Chrome()
            # Test that it exists on the case list
            ch.get(reverse('create_event:list_event'))
            try:
                element = WebDriverWait(self.ch, 10).until(EC.presence_of_element_located(By.ID, "main_navbar"))
            finally:
                self.ch.quit()
            # Test for the nav on the edit page for an individual Meeting (pk=1)
            ch.get(reverse('create_event:event_edit', args='1'))
            try:
                element = WebDriverWait(self.ch, 10).until(EC.presence_of_element_located(By.ID, "main_navbar"))
            finally:
                self.ch.quit()
            # Test for the nav on the details page for an individual meeting (pk=1)
            ch.get(reverse('create_event:event_detail', args='1'))
            try:
                element = WebDriverWait(self.ch, 10).until(EC.presence_of_element_located(By.ID, "main_navbar"))
            finally:
                self.ch.quit()
            # Test for the nav on the 'add a meeting' page
            ch.get(reverse('create_event:add_event'))
            try:
                element = WebDriverWait(self.ch, 10).until(EC.presence_of_element_located(By.ID, "main_navbar"))
            finally:
                self.ch.quit()
            # Test for the nav on the 'add a member to event' page
            ch.get(reverse('create_event:event_add_member'))
            try:
                element = WebDriverWait(self.ch, 10).until(EC.presence_of_element_located(By.ID, "main_navbar"))
            finally:
                self.ch.quit()
