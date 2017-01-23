from django.test import TestCase
from .models import GrievanceAward, GrievanceFiles
from django.core.files import File
from add_case.models import Case
from add_member.models import Person
from spfa_mt import settings
from django.test import Client
import os


class GrievanceFile_UploadTest(TestCase):
    #Valid File
    file_1 = open("test_files_grievance_docs_upload/SmallFile.txt", "r")
    valid_file = File(file=file_1)


    #Invalid File Extension
    file_2 = open("test_files_grievance_docs_upload/Picture.jpg", "r")
    sampleBadExtension = File(file=file_2)


    file_3 = open("test_files_grievance_docs_upload/SmallFile.txt", "r")
    very_large_file = File(file=file_3)
    very_large_file.size = 524288001

    griev_f1 = GrievanceFiles()
    person1 = Person()
    temp_case = Case()


    #Create a grievance award

    griev_aw = GrievanceAward(awardAmount=500,
                              grievanceType='M',
                              case=1,
                              recipient=1,
                              )



    def setUp(self):

        self.griev_aw.save()

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
        self.person1.committee = 'Sample Commitee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

        self.temp_case.lead = 123456789
        self.temp_case.complainant = self.person1
        self.temp_case.campus = "Saskatoon"
        self.temp_case.school = "School of Business"
        self.temp_case.department = "ILDC"
        self.temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        self.temp_case.status = "OPEN"
        self.temp_case.additionalNonMembers = ""
        self.temp_case.docs = None
        self.temp_case.logs = None
        self.temp_case.date = "2016-10-20"
        self.temp_case.full_clean()
        self.temp_case.save()

    def test_user_can_upload_single_grievance_document(self):
        """
        Test if a user can associate a single document to a grievance ruling
        :return: None
        """
        self.griev_f1.file.file = self.valid_file
        self.griev_f1.award = self.griev_aw
        self.griev_f1.save()
        self.assertTrue(self.griev_f1.award == self.griev_aw)



    ''' ANOTHER STORY
    def test_user_can_upload_multiple_grievance_docs(self):
        """
        Test if user can associate multiple documents to a grievance  ruling
        :return: None
        """
        pass
    '''
    def test_user_uploaded_document_is_in_the_correct_path_in_the_server(self):
        """
        Test if user's uploaded document exists in the server
        :return: None
        """

        self.griev_f1.file.file = self.valid_file
        self.griev_f1.award = self.griev_aw
        self.griev_f1.save()
        c = Client()
        response = c.get("http://127.0.0.1:8000/media/files/SmallFile.txt")

        print(response.content)
        # self.assertTrue(self.valid_file.name==path)
        pass



    def test_user_can_upload_if_the_total_file_size_is_less_than_500MB(self):
        """
        Test if user's uploaded file is less than 500Mb
        :return: None
        """
        self.assertTrue(self.samplefile.size < 524288000)


    def test_user_cannot_upload_if_the_total_file_size_is_greater_than_500MB(self):
        """
        Test if users's uploaded file is less than 500MB
        :return: None
        """
        self.assertFalse(self.samplefile.size >= 524288000)

    def test_user_can_upload_files_with_valid_extension(self):
        """
        Test if user's uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
        :return: None
        """
        file = self.samplefile.name.split(".")
        file_extension = file[-1]
        print(file_extension)
        self.assertTrue(file_extension in settings.FILE_EXT_TO_ACCEPT)

    def test_user_can_not_upload_files_with_invalid_extension(self):
        """
        Test if user's uploaded file does not have one of the following extensions:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
        :return: None
        """
        file = self.sampleBadExtension.name.split(".")
        file_extension = file[-1]
        print(file_extension)
        print(settings.FILE_EXT_TO_ACCEPT_STR)
        self.assertFalse(file_extension in settings.FILE_EXT_TO_ACCEPT)


    def test_db_tracks_the_file_upload_date(self):
        """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
        :return: None
        """
        self.griev_f1.file.file = self.samplefile
        self.griev_f1.award = self.griev_aw
        self.griev_f1.save()

        self.assertTrue(self.griev_f1.date_uploaded != "" and self.griev_f1.date_uploaded != None)

    def tearDown(self):
        self.file_1.close()
        self.file_2.close()
        self.file_3.close()