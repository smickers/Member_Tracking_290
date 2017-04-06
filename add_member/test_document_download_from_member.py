from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import Person, MemberFiles
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from spfa_mt import settings
from django.core.files import File
from django.http import HttpResponse
from django.conf.urls import url
from mimetypes import MimeTypes
import os.path
import shutil


@override_settings(MEDIA_ROOT='media/')
class DocumentDownloadTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(DocumentDownloadTestCase, cls).setUpClass()

    # Function: init
    # Purpose: This function is used to initialize the variables used for the tests
    def __init__(self, *args, **kwargs):
        super(DocumentDownloadTestCase, self).__init__(*args, **kwargs)
        # Feels cheap, but why create more bloat in the application? Use what they
        # made back in grievance award file uploads.
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.tempPerson = Person()
        self.path_smallFile = self.CONST_FILE_PATH % 'SmallFile.txt'
        self.path_pptFile = self.CONST_FILE_PATH % 'powerpoint.pptx'
        self.path_excelFile = self.CONST_FILE_PATH % 'excelFile.xlsx'

    def setUp(self):


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

        f = open(self.path_smallFile, "wb")
        f.seek(250)
        f.write("\0")
        f.close()

        f = open(self.path_pptFile, "wb")
        f.seek(250)
        f.write("\0")
        f.close()

        f = open(self.path_excelFile, "wb")
        f.seek(250)
        f.write("\0")
        f.close()

        self.text_file = MemberFiles()
        fp = open(self.path_smallFile, "r")
        self.text_file.fileName = File(fp)
        self.text_file.relatedMember = self.tempPerson
        self.text_file.clean()
        self.text_file.save()
        fp.close()

        self.ppt_file = MemberFiles()
        fp = open(self.path_pptFile, "r")
        self.ppt_file.fileName = File(fp)
        self.ppt_file.relatedMember = self.tempPerson
        self.ppt_file.clean()
        self.ppt_file.save()
        fp.close()

        self.excel_file = MemberFiles()
        fp = open(self.path_excelFile, "r")
        self.excel_file.fileName = File(fp)
        self.excel_file.relatedMember = self.tempPerson
        self.excel_file.clean()
        self.excel_file.save()
        fp.close()

    # Test 1: Test that a file exists for the member (this is the only test that should pass before pre-code, as it's
    # just ensuring the user has files associated with them ... basically mimicking the containsfile() function we
    # created in S16)
    def test_that_a_file_exists_for_the_member(self):
        self.assertTrue(MemberFiles.objects.filter(relatedMember=self.tempPerson.id) != 0)

    # Test 2: Test that a user can download a document from a member profile
    def test_user_can_download_a_document_from_a_member_profile(self):
        client = Client()
        # Response will not get a result until a URL is properly configured for accessing the file at the media root
        response = client.get("/addmember/download/" + str(self.text_file.fileName))
        # Test will pass if the content-disposition header, which is automatically created when you collect a response,
        # matches what is essentially us hard-coding the same thing
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename=' + str(self.text_file.fileName))

    # Test 3: Test that downloaded file's contents are not empty:
    def test_downloaded_file_not_empty(self):
        client = Client()
        # Response will not get a result until a URL is properly configured for accessing the file at the media root
        response = client.get("/addmember/download/" + str(self.text_file.fileName))
        # Have to set the content length header, being the length of the content returned by response
        response['Content-Length'] = len(response.content)
        # Test will pass if the content length isn't null
        self.assertTrue(response['Content-Length'] is not None)

    # Test 4: Test that downloaded content contains the same contents it was saved with
    def test_downloaded_content_has_correct_contents(self):
        client = Client()
        # Response will not get a result until a URL is properly configured for accessing the file at the media root
        response = client.get("/addmember/download/" + str(self.text_file.fileName))
        # Open a file
        f = open("media/" + str(self.text_file.fileName), 'rb')
        # Read all the lines in the file
        lines = f.readlines()
        f.close()
        # Test should pass if the content returned by response, matches what we return in the variable 'lines'
        self.assertEquals( response.content, lines[0])

    # Tear down and trash all the old files
    # def tearDown(self):
    #     if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
    #         shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])

