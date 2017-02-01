from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase
from spfa_mt import settings

from bs4 import BeautifulSoup

"""
    This class contains tests for file uploads on a case information
"""
class CaseFileUpload(TestCase):

    """
        Class constructor
    """
    # def __init__(self):
    #     # self.CONST_FILE_PATH = settings.STATIC_ROOT + 'add_case/test_case_file_upload/%s'
    #     # self.small_text = self.CONST_FILE_PATH % "small_text.txt"
    #     pass
    #
    # """
    #     Set up function
    # """
    # def setUp(self):
    #     # f = open(self.small_text, "wb")
    #     # f.seek(300)
    #     # f.write("\0")
    #     # f.close()
    #     pass



    """
    Test if a user can associate a single document to a case
    """
    def test_user_can_upload_single_case_document(self):
        #Associate the Case object with an actual file

        #Associate Case File object with a case

        #Save the Case File object

        # close file stream

        # Test if there is a file inside the media root directory

        pass


    """
        Test if user's uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
     """
    def test_files_with_valid_file_extension_can_be_uploaded(self):

        # For each Valid File:
            #Associate the Case object with an actual file

            #Associate Case File object with a case

            #Save the Case File object

            # close file stream

            # Test if there is a file inside the media root directory

        pass

    """
    Test if user's uploaded file is less than or equal to 500Mb
    """
    def test_user_can_upload_if_the_file_size_is_less_than_or_equal_500MB(self):

        # Associate the Case object with an actual file ( file size < 500 MB)

        # Associate Case File object with a case

        # Save the Case File object

        # close file stream

        # Test if there is a file inside the media root directory

        pass

    """
    Test if user's uploaded file is less than or equal to 500Mb
    """
    def test_user_cannot_upload_if_file_size_is_greater_than_500MB(self):
        # Test will expect a validation error to occur:

            # Associate the Case object with an actual file

            # Associate Case File object with a case

            # Save the Case File object

            # close file stream

            # Test if there is a file inside the media root directory
        pass


    """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
    """
    def test_db_tracks_the_file_upload_date(self):
        pass

        # Associate the Case object with an actual file

        # Associate Case File object with a case

        # Save the Case File object

        # close file stream

        # Test if there is a file inside the media root directory

        # Test if the Case File object's date attribute is not null



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