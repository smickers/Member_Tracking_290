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

    #TODO: go to this link for download test example
    # "http://stackoverflow.com/questions/8244220/django-unit-test-for-testing-a-file-download"
    def test_that_a_file_exists_for_the_member(self):
        self.assertTrue(MemberFiles.objects.filter(relatedMember=self.tempPerson.id) != 0)


    def test_user_can_download_a_document_from_a_member_profile(self):
        self.client = Client()
        # Weird error with using the file url causes the / betweeen memebrs and files to dissapear
        # hardocing the value in and parsing /membersfiles out of the string
        # response = self.client.get(str(self.text_file))

        # We need to register the url where the files are stored in the urls for the download
        # link to work. Don't think the tests will pass until then
        response = self.client.get("/members/files" + str(self.path_smallFile)[6:])
        print(response)
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename=' + str(self.text_file.fileName))




