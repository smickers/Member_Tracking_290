# SPFA MT CST Project
# February 15, 2017
# Cameron Auser
from spfa_mt import settings
from django.test import TestCase
from .models import contactLog
from add_member.models import Person
from django.core.exceptions import ValidationError
from spfa_mt import kvp
from django.test import override_settings


# Make sure we aren't writing crap data to the same location
# as where the real data lives
@override_settings(MEDIA_ROOT='test/')
class ContactLogEditTests(TestCase):

    cLog = contactLog()
    person1 = Person()
    person2 = Person()
    person3 = Person()
    # Unit test setup method
    def setUp(self):
        # Set up our people
        self.person1.memberID = 4204444
        self.person1.firstName = 'Deborah'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Williams'
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
        self.person1.committee = 'Sample Commitee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

        # Set up the contact log to be edited
        # self.cLog.member = self.person1
        # self.cLog.date = '2017-02-12'
        # self.cLog.description = 'Hello world!'
        # self.cLog.full_clean()
        # self.cLog.save()

        # Put together some sample files
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'add_case/test_case_file_upload/%s'
        self.oversizeFile = self.CONST_FILE_PATH % "COSA190.docx"
        self.undersizeFile = self.CONST_FILE_PATH % "COSC195.docx"
        self.invalidFile = self.CONST_FILE_PATH % "my_C_program.exe"

        f = open(self.oversizeFile, "wb")
        f.seek(settings.MAX_FILE_SIZE + 1)
        f.write("\0")
        f.close()

        f = open(self.undersizeFile, "wb")
        f.seek(settings.MAX_FILE_SIZE - 1)
        f.write("\0")
        f.close()

        f = open(self.invalidFile, "wb")
        f.seek(564)
        f.write("\0")
        f.close()
        pass






    # Test 1: Ensure all valid contact codes are accepted
    def test_valid_contact_codes(self):

        # Loop through all the valid status codes
        for status in kvp.CONTACT_LOG_STATUSES:
            self.cLog = contactLog()
            self.cLog.member = self.person1
            self.cLog.date = '2017-01-01'
            self.cLog.description = 'Example Entry'
            self.cLog.contactCode = status
            self.cLog.clean()
            self.cLog.save()

        # If no exception was raised, this test passed
        self.assertTrue(True)

    # Test 2: Ensure an invalid contact code is not accepted
    def test_invalid_contact_code(self):
        with (self.assertRaisesMessage(ValidationError, "Select an option from the list of choices.")):
            self.cLog.member = self.person1
            self.cLog.date = '2017-01-01'
            self.cLog.description = 'Example Entry'
            self.cLog.contactCode = 'Telegram'
            self.cLog.clean()
            self.cLog.save()

    # Test 3: Ensure all valid file extensions are accepted
    def test_valid_file_extension_are_accepted(self):
        print("ayy")