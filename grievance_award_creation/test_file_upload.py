from django.test import TestCase
from .models import GrievanceAward, GrievanceFiles
from django.core.files import File
from add_case.models import Case
from add_member.models import Person

class GrievanceFile_UploadTest(TestCase):
    samplefile = File(name='Hello', file=None)
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
        self.samplefile.size = 1000

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
        self.temp_case.department = "Business Certificate"
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

        """
        self.griev_f1.file.file = self.samplefile
        self.griev_f1.award = self.griev_aw
        self.griev_f1.save()
        """


    def test_user_can_upload_multiple_grievance_docs(self):
        """
        Test if user can associate multiple documents to a grievance  ruling
        :return: None
        """
        pass

    def test_user_uploaded_document_is_in_the_correct_path_in_the_server(self):
        """
        Test if user's uploaded document exists in the server
        :return: None
        """
        pass

    def test_user_can_upload_if_the_total_file_size_is_less_than_500MB(self):
        """
        Test if user's uploaded file is less than 500Mb
        :return: None
        """
        pass


    def test_user_cannot_upload_if_the_total_file_size_is_greater_than_500MB(self):
        """
        Test if users's uploaded file is less than 500MB
        :return: None
        """
        pass

    def test_user_can_only_upload_files_with_valid_extension(self):
        """
        Test if user's uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
        :return: None
        """
        pass

    def test_db_tracks_the_file_upload_date(self):
        """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
        :return: None
        """
        pass

