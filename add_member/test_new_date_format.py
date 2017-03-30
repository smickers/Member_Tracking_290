from django.test import TestCase, Client, LiveServerTestCase
from django.urls import reverse
from .models import Person

class DateFormatTestCase(LiveServerTestCase):
    def setUp(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.pCode = 's7k5j8'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()

    #Test that the date is loading in the proper format in the proper format
    def test_proper_date_format_is_loading(self):
        person_to_edit = Person.objects.filter(memberID=123456789)[0]
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get(reverse('add_member:member_update', kwargs={'pk': person_to_edit.pk}),)
        # Get the initial values found in the model & view
        #print(response.context)
        oldresponsevalues = response.context['form']
        self.assertRegexpMatches(oldresponsevalues.__str__(),
                    # This regular expression searches for date selectors to load in Day, Month, Year
                    "^(?s).*(id_bDay_day).(?s).*(id_bDay_month)(?s).*(id_bDay_year)(?s).*$")

    # Test that the date is not loading in the unproper format
    def test_old_format_is_not_loading(self):
        person_to_edit = Person.objects.filter(memberID=123456789)[0]
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get(reverse('add_member:member_update', kwargs={'pk': person_to_edit.pk}))
        # Get the initial values found in the model & view
        # print(response.context)
        oldresponsevalues = response.context['form']
        self.assertNotRegexpMatches(oldresponsevalues.__str__(),
                # This regular expression searches for date selectors to load in Day, Month, Year
                "^(?s).*(id_bDay_month).(?s).*(id_bDay_day)(?s).*(id_bDay_year)(?s).*$")
