from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import *
from add_member.models import Person
from add_case.models import *
from django.db import DataError
import datetime
from django.test import override_settings
from spfa_mt import settings
from django.core.files import File
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client


# FileViewTests
# This tests to make sure that the user can properly see the file associated
# with a grievance award
@override_settings(MEDIA_ROOT='test/')
class FileViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(FileViewTests, cls).setUpClass()

    def __init__(self, *args, **kwargs):
        super(FileViewTests, self).__init__(*args, **kwargs)

        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.path_docfile = self.CONST_FILE_PATH % 'Document.docx'
        self.ga = GrievanceAward()
        self.ga2 = GrievanceAward()
        self.tempCase = Case()
        self.tempCase2 = Case()
        self.tempPerson = Person()
        self.tempPerson2 = Person()
        self.program = CasePrograms()
        self.grievance_files = GrievanceFiles()

    def setUp(self):
        # Set up a program
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

        # Set up a Member for testing
        self.tempPerson.memberID = 1
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

        # Set up second member for testing
        self.tempPerson2.memberID = 1
        self.tempPerson2.firstName = 'Test'
        self.tempPerson2.middleName = 'This'
        self.tempPerson2.lastName = 'Person'
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

        # Set up a case for testing
        self.tempCase = Case()
        self.tempCase.lead = self.tempPerson.id
        self.tempCase.complainant = self.tempPerson
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.program = self.program
        self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase.status = "OPEN"
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()

        # Set up a second Case for testing
        self.tempCase2 = Case()
        self.tempCase2.lead = self.tempPerson.id
        self.tempCase2.complainant = self.tempPerson
        self.tempCase2.campus = "Saskatoon"
        self.tempCase2.school = "School of Business"
        self.tempCase2.program = self.program
        self.tempCase2.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase2.status = "OPEN"
        self.tempCase2.date = "2016-10-20"
        self.tempCase2.full_clean()
        self.tempCase2.save()

        # Set up a grievence award to be edited
        self.ga.grievanceType = "M"
        self.ga.recipient = self.tempPerson
        self.ga.case = self.tempCase
        self.ga.awardAmount = 500.00
        self.ga.description = ""
        self.ga.date = '2016-12-01'
        self.ga.full_clean()
        self.ga.save()

        # Set up a grievence award to be edited
        self.ga2.grievanceType = "M"
        self.ga2.recipient = self.tempPerson
        self.ga2.case = self.tempCase
        self.ga2.awardAmount = 500.00
        self.ga2.description = ""
        self.ga2.date = '2016-12-01'
        self.ga2.full_clean()
        self.ga2.save()

        f = open(self.path_docfile, "wb")
        f.seek(300)
        f.write("\0")
        f.close()

        path = (settings.STATIC_ROOT + "grievance_award_creation/test_files_grievance_docs_upload/SmallFile.txt")
        fp = open(path, "r")

        # Associate the Grievance File object with an actual file
        self.grievance_files.file = File(fp)

        # Associate an award witha file
        self.grievance_files.award = self.ga

        # Save the file
        self.grievance_files.full_clean()
        self.grievance_files.save()

        # #close file stream
        fp.close()

    # Ensuring that the file was uploaded so we can test it.
    def test_file_exists(self):
        assert self.grievance_files.award == self.ga

    # This checks the html to see if the file shows up on the award detail page
    def test_user_sees_the_file_associated_to_the_award(self):
        client = Client()
        response = client.get('/grievance/detail/{}'.format(self.ga.id))
        file_name = self.grievance_files.file.__str__().split('/')
        self.assertTrue(file_name[4] in response.content)
        self.assertTrue(response.content.__contains__("Documents:"))
        self.assertTrue(response.content.__contains__("Document Description:"))
        self.assertTrue(response.content.__contains__("Document Upload Date:"))

    # Checking to see that the user doesn't see a file when an award doesn't have one
    def test_award_with_no_file_shows_no_file(self):
        client = Client()
        response = client.get('/grievance/detail/{}'.format(self.ga2.id))
        self.assertFalse(response.content.__contains__("Documents:"))
        self.assertFalse(response.content.__contains__("Document Description:"))
        self.assertFalse(response.content.__contains__("Document Upload Date:"))

    # Make a test to check that the icon is being displayed to the use
