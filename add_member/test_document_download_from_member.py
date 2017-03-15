from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import Person, MemberFiles
from spfa_mt import settings
from django.core.files import File
from django.http import HttpResponse
from django.conf.urls import url
from mimetypes import MimeTypes



class DocumentDownloadTestCase(TestCase):

    def setUp(self):
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.tempPerson = Person()
        self.path_smallFile = self.CONST_FILE_PATH % 'SmallFile.txt'
        self.path_pptFile = self.CONST_FILE_PATH % 'powerpoint.pptx'
        self.path_excelFile = self.CONST_FILE_PATH % 'excelFile.xlsx'

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
        # client = Client()
        # Weird error with using the file url causes the / between members and files to disappear
        # hard-coding the value in and parsing /MemberFiles out of the string
        # response = self.client.get(str(self.text_file))

        #print(self.client.get(self.text_file))
        # We need to register the url where the files are stored in the urls for the download
        # link to work. Don't think the tests will pass until then
        #response2 = self.client.get("/members/files/" + str(self.path_smallFile)[6:])
        # print("/members/files/" + str(self.path_smallFile)[6:])
        # print("/" + self.path_smallFile)
        response2 = self.client.get("/members/" + str(self.path_smallFile))
        # print(response2)
        # Steph's note: Got this working below. Our biggest problem is when a file is a duplicate, it's appending a
        # random string to the file name.
        wrapper = FileWrapper(file(self.path_smallFile, "rb"))
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % str(self.text_file.fileName)
        print(str(self.text_file.file.url))
        # print(response)
        response
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename=')

    # Test 3: Test that downloaded file's contents are not empty:
    def test_downloaded_file_not_empty(self):
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % str(self.text_file.fileName)
        response['X-Sendfile'] = self.text_file.fileName
        self.assertTrue(response['Content-Length'] is not None)

    # Test 4: Test that downloaded content contains the same contents it was saved with
    def test_downloaded_content_has_correct_contents(self):
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % str(self.text_file.fileName)


