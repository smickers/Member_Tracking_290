from .models import GrievanceAward, GrievanceFiles
from django.core.files import File
from add_case.models import Case
from add_member.models import Person
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ValidationError
from spfa_mt import settings
from datetime import datetime
import shutil
import os.path



@override_settings(MEDIA_ROOT='test/')
class GrievanceFile_UploadTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(GrievanceFile_UploadTest, cls).setUpClass()

    def __init__(self, *args, **kwargs):
        super(GrievanceFile_UploadTest, self).__init__(*args, **kwargs)
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.person1 = Person()
        self.temp_case = Case()
        self.grievance_files = GrievanceFiles()
        self.griev_aw = None

        self.path_largefile = self.CONST_FILE_PATH % 'dummylarge.txt'
        self.path_notsolargefile= self.CONST_FILE_PATH % 'notsolarge.txt'
        self.path_picturefile = self.CONST_FILE_PATH % 'Picture.jpg'


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

        self.griev_aw = GrievanceAward(awardAmount=500,
                                  grievanceType='M',
                                  case=self.temp_case,
                                  recipient=self.person1)
        self.griev_aw.save()

        f = open(self.path_largefile, "wb")
        f.seek(settings.MAX_FILE_SIZE+1)
        f.write("\0")
        f.close()


        f = open(self.path_notsolargefile, "wb")
        f.seek(settings.MAX_FILE_SIZE-1)
        f.write("\0")
        f.close()

    def test_user_can_upload_single_grievance_document(self):
        """
        Test if a user can associate a single document to a grievance ruling
        :return: None
        """
        path = (settings.STATIC_ROOT + "grievance_award_creation/test_files_grievance_docs_upload/SmallFile.txt")
        fp = open(path, "r")

        #Associate the Grievance File object with an actual file
        self.grievance_files.file = File(fp)

        #Associate an award witha file
        self.grievance_files.award = self.griev_aw


        #Save the file
        self.grievance_files.full_clean()
        self.grievance_files.save()

        # #close file stream
        fp.close()

        # Test if there is a file inside the media root directory
        self.assertTrue( os.listdir(self._overridden_settings["MEDIA_ROOT"] + "/grievance").__len__() > 0)



    def test_user_can_upload_if_the_file_size_is_less_than_500MB(self):
        """
        Test if user's uploaded file is less than 500Mb
        :return: None
        """
        path = self.path_notsolargefile
        fp = open(path, "r")

        # Associate the Grievance File object with an actual file
        self.grievance_files.file = File(fp)

        # Associate an award witha file
        self.grievance_files.award = self.griev_aw

        # Save the file
        self.grievance_files.full_clean()
        self.grievance_files.save()

        # #close file stream
        fp.close()

        # Test if there is a file inside the media root directory
        print(self.grievance_files.file.size)

        self.assertTrue(self.grievance_files.file.size <= settings.MAX_FILE_SIZE)

    def test_user_cannot_upload_if_the_total_file_size_is_greater_than_500MB(self):
        """
        Test if users's uploaded file is less than 500MB
        :return: None
        """

        with self.assertRaises(ValidationError):
            """
                Expects the statement below to throw a validation error
            """
            path = self.path_largefile
            fp = open(path, "r")

            # Associate the Grievance File object with an actual file
            self.grievance_files.file = File(fp)

            # Associate an award with a file
            self.grievance_files.award = self.griev_aw

            # Save the file
            self.grievance_files.full_clean()
            self.grievance_files.save()

            # #close file stream
            fp.close()




    def test_user_can_not_upload_files_with_invalid_extension(self):
        """
        Test if user's uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
        :return: None
        """
        with self.assertRaises(ValidationError):
            """Expects validation error"""
            path = self.path_picturefile
            fp = open(path, "r")

            # Associate the Grievance File object with an actual file
            self.grievance_files.file = File(fp)

            # Associate an award witha file
            self.grievance_files.award = self.griev_aw

            # Save the file
            self.grievance_files.full_clean()
            self.grievance_files.save()

            # #close file stream
            fp.close()




    def test_db_tracks_the_file_upload_date(self):
        """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
        :return: None
        """
        path = self.path_notsolargefile
        fp = open(path, "r")

        # Associate the Grievance File object with an actual file
        self.grievance_files.file = File(fp)

        # Associate an award witha file
        self.grievance_files.award = self.griev_aw

        # Save the file
        self.grievance_files.full_clean()
        self.grievance_files.save()

        # #close file stream
        fp.close()

        #Check if the minute the file saved is the same time as the actual time
        self.assertTrue(self.grievance_files.date_uploaded != None)




    def tearDown(self):
        if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
            shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])

        """Doesnt work on windows"""
        # dummyfiles = ['dummylarge.txt', 'notsolarge.txt']
        # for i in dummyfiles:
        #     if os.path.exists(self.CONST_FILE_PATH%i):
        #         os.remove(self.CONST_FILE_PATH%i)