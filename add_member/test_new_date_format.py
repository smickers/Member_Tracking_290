from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Person

class DateFormatTestCase(TestCase):
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

    #Exception Test 42 - Test if user cannot leave campus field empty
    def test_date_format(self):
        person_to_edit = Person.objects.filter(memberID=123456789)[0]
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get('/member/update/' + str(person_to_edit.pk) + '/')
        # Get the initial values found in the model & view
        # print(response.context)
        oldresponsevalues = response.context['form']
        print(oldresponsevalues)
        # # Override the old set of values with the desired one
        # oldresponsevalues["campus"] = ""
        # # DO a post method to send the newly created dataset
        # response = client.post('/member/update/' + str(person_to_edit.pk) + '/', oldresponsevalues)
        # # Do a query for the object that you want to compare
        # person_to_edit = Person.objects.filter(memberID=123456789)[0]
        # self.assertContains(response, "This field is required", 1, 200)