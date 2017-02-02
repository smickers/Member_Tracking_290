from django.db import IntegrityError
from django.core.exceptions import ValidationError
from spfa_mt import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files import File
from .models import Case
from add_member.models import Person
from django.test import override_settings
import os



"""
    This class contains tests for file uploads on a case information
"""
@override_settings(MEDIA_ROOT='test/')
class CaseFileUpload(StaticLiveServerTestCase):

    """
        Class constructor
        Assumptions:
            CaseFiles - model for case file object
                * date_uploaded
                * file
                * description
                * case
    """



    """
        Set up function
    """
    def setUp(self):
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'add_case/test_case_file_upload/%s'
        self.small_text = self.CONST_FILE_PATH % "small_text.txt"

        # create a dummy case file.

        self.sample_casefile = CaseFiles()


        self.person1 = Person()
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


        self.case = Case()
        self.case.lead = 123456789
        self.case.complainant = self.person1
        self.case.campus = "Saskatoon"
        self.case.school = "School of Business"
        self.case.program = self.prog
        self.case.caseType = "GRIEVANCES - CLASSIFICATION"
        self.case.status = "OPEN"
        self.case.docs = None
        self.case.logs = None
        self.case.date = "2016-10-20"
        self.case.full_clean()
        self.case.save()

        #TODO: add a python command that will create files/addcase/test_case_file_upload folder.

        f = open(self.small_text, "wb")
        f.seek(300)
        f.write("\0")
        f.close()
        pass



    """
    Test if a user can associate a single document to a case
    """
    def test_user_can_upload_single_case_document(self):

        # Open the file
        path = (self.small_text)
        fp = open(path, "r")


        #Associate the Case object with an actual file
        self.sample_casefile.file = File(fp)

        #Associate Case File object with a case
        self.sample_casefile.case = self.case

        #Save the Case File object
        self.sample_casefile.save()

        # close file stream
        fp.close()

        # Test if there is a file inside the media root directory

        self.assertTrue( os.listdir(self._overridden_settings["MEDIA_ROOT"] + "/case").__len__() > 0)



    """
        Test if user's uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
     """
    def test_files_with_valid_file_extension_can_be_uploaded(self):
        list_of_accepted_files = settings.FILE_EXT_TO_ACCEPT

        # For each Valid File:
        for extension in list_of_accepted_files:

            # generate a filename
            file_name = "file_name.%s" % extension

            # build the file path
            file_path = self.CONST_FILE_PATH % file_name

            # open the file
            f = open(file_path, "w")
            f.seek(2)
            f.write("HI")
            # close the file stream
            f.close()

            # Open the file
            fp = open(file_path, "r")

            # Associate the Case object with an actual file
            self.sample_casefile.file = File(fp)

            # Associate Case File object with a case
            self.sample_casefile.case = self.case

            # Save the Case File object
            self.sample_casefile.save()

            # close file stream
            fp.close()

            # Test if there is a file inside the media root directory
            self.assertTrue(os.path.isfile(file_path))


    """
    Test if user's uploaded file is less than or equal to 500Mb
    """
    def test_user_can_upload_if_the_file_size_is_less_than_or_equal_500MB(self):

        # Create a 500 Megabyte file
        path_to_a_500_file = self.CONST_FILE_PATH % "500_MB_file.txt"
        f = open(path_to_a_500_file, "wb")
        f.seek(settings.MAX_FILE_SIZE)
        f.write("\0")
        f.close()


        # Open the file
        fp = open(path_to_a_500_file, "r")


        #Associate the Case object with an actual file
        self.sample_casefile.file = File(fp)

        #Associate Case File object with a case
        self.sample_casefile.case = self.case

        #Save the Case File object
        self.sample_casefile.save()

        # close file stream
        fp.close()

        # Test if there is a file inside the media root directory

        self.assertTrue(os.path.isfile(path_to_a_500_file))

    """
    Test if user's uploaded file is less than or equal to 500Mb
    """
    def test_user_cannot_upload_if_file_size_is_greater_than_500MB(self):

        path_to_over_500_MB_file = self.CONST_FILE_PATH % "over_500_MB_file.txt"
        f = open(path_to_over_500_MB_file, "wb")
        f.seek(settings.MAX_FILE_SIZE + 1)
        f.write("\0")
        f.close()


        # Test will expect a validation error to occur:
        with self.assertRaises(ValidationError):
            # Open the file
            fp = open(path_to_over_500_MB_file, "r")


            #Associate the Case object with an actual file
            self.sample_casefile.file = File(fp)

            #Associate Case File object with a case
            self.sample_casefile.case = self.case

            #Save the Case File object
            self.sample_casefile.save()

            # close file stream
            fp.close()

    """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
    """
    def test_db_tracks_the_file_upload_date(self):
        # Open the file
        path = (self.small_text)
        fp = open(path, "r")


        #Associate the Case object with an actual file
        self.sample_casefile.file = File(fp)

        #Associate Case File object with a case
        self.sample_casefile.case = self.case

        #Save the Case File object
        self.sample_casefile.save()

        # close file stream
        fp.close()

        # Test if the Case File object's date attribute is not null
        self.assertTrue(self.sample_casefile.date_uploaded is not None)





    # """
    # Function: tearDown
    # Purpose: Deletes Temproary files after tests completed.
    # NOTE: Due to multiple processes running by Django, this only works in Linux
    # """
    # def tearDown(self):
    #     if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
    #         shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])
    #
    #     """Doesnt work on windows"""
    #     # dummyfiles = ['dummylarge.txt', 'notsolarge.txt']
    #     # for i in dummyfiles:
    #     #     if os.path.exists(self.CONST_FILE_PATH%i):
    #     #         os.remove(self.CONST_FILE_PATH%i)