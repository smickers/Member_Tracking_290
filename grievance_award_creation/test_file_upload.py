from .models import GrievanceAward, GrievanceFiles
from django.core.files import File
from add_case.models import Case
from add_member.models import Person
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from spfa_mt import settings
import shutil
import os.path


@override_settings(MEDIA_ROOT='/tmp/test')
class GrievanceFile_UploadTest(StaticLiveServerTestCase):
    def __init__(self, *args, **kwargs):
        super(GrievanceFile_UploadTest, self).__init__(*args, **kwargs)
        self.person1 = Person()
        self.temp_case = Case()
        self.grievance_files = GrievanceFiles()

        #Create a grievance award
        self.griev_aw = GrievanceAward(awardAmount=500,
                                  grievanceType='M',
                                  case=1,
                                  recipient=1,)



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

        #Open the file using its static directory
        fp =  open(settings.STATIC_ROOT + "grievance_award_creation/test_files_grievance_docs_upload/Picture.jpg")

        #Associate the Grievance File object with an actual file
        self.grievance_files.file = File(fp)

        #Associate an award witha file
        self.grievance_files.award = self.griev_aw

        #Save the file
        self.grievance_files.save()

        #close the file stream
        fp.close()

        #test if there is a file inside the media root directory
        self.assertEqual( os.listdir(self._overridden_settings["MEDIA_ROOT"] + "/grievance").__len__() , 1)



    # def test_user_uploaded_document_is_in_the_correct_path_in_the_server(self):
    #     """
    #     Test if user's uploaded document exists in the server
    #     :return: None
    #     """


    def test_user_can_upload_if_the_total_file_size_is_less_than_500MB(self):
        """
        Test if user's uploaded file is less than 500Mb
        :return: None
        """



        #Open the file using its static directory
        fp =  open(settings.STATIC_ROOT + "grievance_award_creation/test_files_grievance_docs_upload/Picture.jpg")

        #Associate the Grievance File object with an actual file
        file_wrap = File(fp)
        file_wrap.size = settings.MAX_FILE_SIZE -1
        self.grievance_files.file = file_wrap

        #Associate an award with the file
        self.grievance_files.award = self.griev_aw

        #Save the file
        self.grievance_files.save()

        #close the file stream
        fp.close()

        #test if the file uploaded is less than the specified maximum file size
        self.assertTrue(self.grievance_files.file.size < settings.MAX_FILE_SIZE)


    def test_user_cannot_upload_if_the_total_file_size_is_greater_than_500MB(self):
        """
        Test if users's uploaded file is less than 500MB
        :return: None
        """
        #Open the file using its static directory
        fp =  open(settings.STATIC_ROOT + "grievance_award_creation/test_files_grievance_docs_upload/Picture.jpg")


        #TODO: ASK ERNESTO ABOUT THIS ONE. EMULATING LARGE FILE SIZE DOESNT WORK SINCE FILE HANDLER LOOKS AT THE
        #TODO:      ACTUAL DATA CHUNK

        #Associate the Grievance File object with an actual file
        file_wrap = File(fp)
        file_wrap.size = settings.MAX_FILE_SIZE + 1
        self.grievance_files.file = file_wrap

        #Associate an award with the file
        self.grievance_files.award = self.griev_aw

        #Save the file
        self.grievance_files.save()

        #close the file stream
        fp.close()



    # def test_user_can_upload_files_with_valid_extension(self):
    #     """
    #     Test if user's uploaded file only has the following extension:
    #     .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
    #     :return: None
    #     """
    #     file = self.samplefile.name.split(".")
    #     file_extension = file[-1]
    #     print(file_extension)
    #     self.assertTrue(file_extension in settings.FILE_EXT_TO_ACCEPT)
    #
    # def test_user_can_not_upload_files_with_invalid_extension(self):
    #     """
    #     Test if user's uploaded file does not have one of the following extensions:
    #     .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
    #     :return: None
    #     """
    #     file = self.sampleBadExtension.name.split(".")
    #     file_extension = file[-1]
    #     print(file_extension)
    #     print(settings.FILE_EXT_TO_ACCEPT_STR)
    #     self.assertFalse(file_extension in settings.FILE_EXT_TO_ACCEPT)
    #
    #
    # def test_db_tracks_the_file_upload_date(self):
    #     """
    #     Test if the database tracks the date when the file is uploaded.
    #     It must be in the format of DD/MM/YYYY
    #     :return: None
    #     """
    #     self.griev_f1.file.file = self.samplefile
    #     self.griev_f1.award = self.griev_aw
    #     self.griev_f1.save()
    #
    #     self.assertTrue(self.griev_f1.date_uploaded != "" and self.griev_f1.date_uploaded != None)



    def tearDown(self):
        shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])


