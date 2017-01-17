from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import *
from django.db import DataError
import datetime
from add_member.models import Person
from django.test import Client, SimpleTestCase, TestCase, LiveServerTestCase
import requests
from bs4 import BeautifulSoup



class CaseTests(TestCase):
    person1 = Person()
    satellite = CaseSatellite()
    program = CasePrograms()

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

        self.satellite.name = "S - Fourth Ave - SPAO"
        self.satellite.full_clean()
        self.satellite.save()

        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

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
        tempCase.school = "School of Information and Communications Technology"
        tempCase.program = self.program
        tempCase.caseType = "COMPLAINT"
        tempCase.status = "OPEN"
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
    def test_satellite_location_saves_when_it_is_50_characters(self):
        tempCase = Case()
        tempCase.lead = 1
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.satellite = 'a' * 50
        tempCase.school = "School of Information and Communications Technology"
        tempCase.program = self.program
        tempCase.caseType = "COMPLAINT"
        tempCase.status = "OPEN"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()


    '''
    Name:       test_satellite_location_does_not_save_when_it_is_over_50_characters
    Function:   Makes sure that the satellite is not saved when the text is over 50 characters. For this test, we will
                be using 51 characters.
    '''
    def test_satellite_location_does_not_save_when_it_is_over_50_characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 1
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.satellite = 'a' * 51
            tempCase.school = "School of Information and Communications Technology"
            tempCase.program = self.program
            tempCase.caseType = "COMPLAINT"
            tempCase.status = "OPEN"
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

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
        tempCase.school = "School of Information and Communications Technology"
        tempCase.program = self.program
        tempCase.caseType = "COMPLAINT"
        tempCase.status = "OPEN"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    '''
    Name:       test_that_the_lists_have_correct_values
    Function:   Make sure the lists are populated correctly. It is done in one test to reduce the amount of requests
    '''
    def test_that_lists_have_correct_values(self):
        # WARNING, THIS TEST REQUIRES THE SERVER TO BE STARTED
        # This first part checks for the campus list
        source_code = requests.get('http://127.0.0.1:8000/addCase/')
        soup = BeautifulSoup(source_code.text, "html.parser")
        campus_list = "Saskatoon\nRegina\nMoose Jaw\nPrince Albert"
        self.assertTrue(soup.text.__contains__(campus_list))

        # Checking the School list
        school_list = "School of Business\nSchool of Construction\nSchool of Health Sciences\nSchool of Human Services and Community Safety"\
            "\nSchool of Information and Communications Technology\nSchool of Mining, Energy and Manufacturing"\
            "\nSchool of Natural Resources and Built Environment\nSchool of Nursing\nSchool of Transportation\nOther"
        self.assertTrue(soup.text.__contains__(school_list))

        # Checking the Department list
        department_list = "Learning Technologies\nILDC\nLibrary\nPLAR\nSimulation Lab\nStudent Development\nLearning Services\nFitness Centre"
        self.assertTrue(soup.text.__contains__(department_list))

        # Checking the type list
        type_list = "GRIEVANCES - INDIVIDUAL\nGRIEVANCES - GROUP\nGRIEVANCES - POLICY\nGRIEVANCES - CLASSIFICATION"\
            "\nGRIEVANCES - COMPLAINTS\nDISABILITY CLAIMS\nARBITRATION\nCOMPLAINT"
        self.assertTrue(soup.text.__contains__(type_list))

        # Checking the status list
        status_list = "OPEN\nCLOSED\nPENDING\nACTION REQ'D - MGMT\nACTION REQ'D SPFA"
        self.assertTrue(soup.text.__contains__(status_list))


    '''
    Name:       test_that_department_saves_and_does_not_have_a_program
    Function:   Makes sure that when a department is entered, a program is not saved as well.
    '''
    def test_that_department_saves_and_does_not_have_a_program(self):
        tempCase = Case()
        tempCase.lead = 1
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.satellite = None
        tempCase.school = "Other"
        tempCase.department = "Learning Technologies"
        tempCase.caseType = "COMPLAINT"
        tempCase.status = "OPEN"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        assert tempCase.program is None
        assert tempCase.department == "Learning Technologies"

    '''
    Name:       test_that_program_saves_and_does_not_have_a_department
    Function:   Makes sure that when a program is entered, a department is not saved as well.
    '''
    def test_that_program_saves_and_does_not_have_a_department(self):
        tempCase = Case()
        tempCase.lead = 1
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.satellite = None
        tempCase.school = "Other"
        tempCase.program = self.program
        tempCase.caseType = "COMPLAINT"
        tempCase.status = "OPEN"
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        assert tempCase.program == self.program
        assert tempCase.department is None
