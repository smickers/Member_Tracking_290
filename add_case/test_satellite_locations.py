from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import *
from django.db import DataError
import datetime
from add_member.models import Person



class CaseTests(TestCase):
    person1 = Person()
    satellite = CaseSatellite()


    '''
    Setting up a person to be used as the primary complainant
    '''
    def setUp(self):
        self.person1.memberID = 4204444
        self.person1.firstName = 'First'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Last'
        self.person1.socNum = 123456789
        self.person1.city = 'Sample City'
        self.person1.mailAddress = 'Sample address'
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

        self.satellite.name = "S - Alberta Ave"
        self.satellite.full_clean()
        self.satellite.save()



    '''
    Name:       test_satellite_location_saves_when_it_is_on_the_preset_list
    Function:   Makes sure the satellite location is saved to the database
                when an option from the list is chosen. Verifies to see if the entry is correct.
    '''
    def test_satellite_location_saves_when_it_is_on_the_preset_list(self):
            tempCase = Case()
            tempCase.lead = 1
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.satellite = self.satellite
            tempCase.school = "OTH"
            tempCase.department = "LIB"
            tempCase.caseType = "G-CLASS"
            tempCase.status = "O"
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()


    '''
    Name:       test_satellite_location_saves_when_it_is_less_than_50_characters
    Function:   Makes sure that the satellite saves to the database when the text is 50 characters or shorter.
                For this test, we will be using 50 characters. Verifies to see if the entry is correct.
    '''
    def test_satellite_location_saves_when_it_is_less_than_50_characters(self):
        pass


    '''
    Name:       test_satellite_location_does_not_save_when_it_is_over_50_characters
    Function:   Makes sure that the satellite is not saved when the text is over 50 characters. For this test, we will
                be using 51 characters.
    '''
    def test_satellite_location_does_not_save_when_it_is_over_50_characters(self):
        pass

    '''
    Name:       test_satellite_location_is_optional_and_case_saved_when_empty
    Function:   Makes sure that the satellite can be blank and the case is still saved to the database.
    '''
    def test_satellite_location_is_optional_and_case_saved_when_empty(self):
        tempCase = Case()
        tempCase.lead = 1
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.satellite = None
        tempCase.school = "OTH"
        tempCase.department = "LIB"
        tempCase.caseType = "G-CLASS"
        tempCase.status = "O"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    '''
    Name:
    Function:   Make sure the lists are populated correctly.
    '''