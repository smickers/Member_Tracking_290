from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import Person, MemberFiles
from spfa_mt import settings
from django.core.files import File
from django.conf.urls import url

class DocumentDownloadTestCase(TestCase):
    def __init__(self, *args, **kwargs):
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

        text_file = MemberFiles()
        fp = open(self.path_smallFile, "r")
        text_file.fileName = File(fp)
        text_file.relatedMember = self.tempPerson
        text_file.clean()
        text_file.save()
        fp.close()

        ppt_file = MemberFiles()
        fp = open(self.path_pptFile, "r")
        ppt_file.fileName = File(fp)
        ppt_file.relatedMember = self.tempPerson
        ppt_file.clean()
        ppt_file.save()
        fp.close()

        excel_file = MemberFiles()
        fp = open(self.path_excelFile, "r")
        excel_file.fileName = File(fp)
        excel_file.relatedMember = self.tempPerson
        excel_file.clean()
        excel_file.save()
        fp.close()

    #TODO: go to this link for download test example
    # "http://stackoverflow.com/questions/8244220/django-unit-test-for-testing-a-file-download"
    def test_that_a_file_exists_form_the_member(self):
        self.assertTrue(self.MemberFiles.objects.filter(relatedMember=self.tempPerson.id) != 0)


    def test_user_can_download_a_document_from_a_member_profile(self):
        self.client = Client()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



