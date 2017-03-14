from .models import Person, MemberFiles
from django.core.files import File
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ValidationError
from spfa_mt import settings
import os.path
import shutil


# Class: MemberFile_UploadTest
# This class is for testing file uploads for a member
@override_settings(MEDIA_ROOT='test/')
class MemberFileUploadTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MemberFileUploadTest, cls).setUpClass()

    # Function: init
    # Purpose: This function is used to initialize the variables used for the tests
    def __init__(self, *args, **kwargs):
        super(MemberFileUploadTest, self).__init__(*args, **kwargs)
        # Feels cheap, but why create more bloat in the application? Use what they
        # made back in grievance award file uploads.
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.person1 = Person()
        self.MemberFile = MemberFiles()
        self.path_largeFile = self.CONST_FILE_PATH % 'dummylarge.txt'
        self.path_midsizedFile = self.CONST_FILE_PATH % 'notsolarge.txt'
        self.path_smallFile = self.CONST_FILE_PATH % 'SmallFile.txt'
        self.path_invalidFile = self.CONST_FILE_PATH % 'invalid.exe'
        self.path_emptyFile = self.CONST_FILE_PATH % 'emptyFile.txt'

    # Function: setUp
    # Purpose: Used to set up testing for a file upload
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

        f = open(self.path_largeFile, "wb")
        f.seek(settings.MAX_FILE_SIZE + 1)
        f.write("\0")
        f.close()

        f = open(self.path_midsizedFile, "wb")
        f.seek(25000)
        f.write("\0")
        f.close()

        f = open(self.path_smallFile, "wb")
        f.seek(250)
        f.write("\0")
        f.close()

        f = open(self.path_invalidFile, "wb")
        f.seek(25000)
        f.write("\0")
        f.close()

        f = open(self.path_emptyFile, "wb")
        f.close()

    # Test 1: that a user can upload a document to a member
    # Also Test 2: test a user can upload a file < 500 MB
    def test_user_can_upload_document_of_valid_file_size_to_member(self):
        # Create a new instance of MemberFiles to associate the File to
        member_file = MemberFiles()
        # Open a regular sized file, since this is a valid file test:
        fp = open(self.path_midsizedFile, "r")
        # Associate the MemberFile with the File we just opened:
        member_file.fileName = File(fp)
        # Associate the MemberFile with a Member, since MF is a join:
        member_file.relatedMember = self.person1
        # Call the clean method of the model, to do file validation:
        member_file.clean()
        # Save the MemberFile object
        member_file.save()
        # close the file stream
        fp.close()
        # Assert that the file exists, meaning our test passes
        self.assertTrue(MemberFiles.objects.filter(fileName=member_file.fileName) != 0)

    # Test 3: Test that a user cannot upload a document > 500MB to a member
    def test_user_cannot_upload_oversize_file_to_member(self):
        with self.assertRaisesRegexp(ValidationError, "Upload size limit exceeded exception"):
            # Create a new instance of MemberFiles to associate the File to
            member_file = MemberFiles()
            # Open an oversized file:
            fp = open(self.path_largeFile, "r")
            # Associate the MemberFile with the File we just opened:
            member_file.fileName = File(fp)
            # Associate the MemberFile with a Member, since MF is a join:
            member_file.relatedMember = self.person1
            # Call the clean method of the model, to do file validation:
            member_file.clean()
            # (Attempt to) Save the MemberFile object
            member_file.save()
            # close the file stream
            fp.close()
            # Assert that the file exists, meaning our test passes
            self.assertTrue(MemberFiles.objects.filter(fileName=member_file.fileName) != 0)

    # Test 4: Test that a user can upload files with valid file extensions
    def test_user_can_upload_file_with_valid_file_extension(self):
        accepted_file_extensions = settings.FILE_EXT_TO_ACCEPT
        for ext in accepted_file_extensions:
            # Create a file name for each extension in the list
            valid_file = "valid_data.%s" % ext
            # Build the file path, and create the file
            file_path = self.CONST_FILE_PATH % valid_file
            f = open(file_path, "wb")
            f.seek(5)
            f.write("\0")
            f.close()
            # Create a new MemberFiles object
            member_file = MemberFiles()
            # Open the file we created
            fp = open(file_path, "r")
            # Associate the MF with the file we created
            member_file.fileName = File(fp)
            member_file.relatedMember = self.person1
            # Call the clean() method to ensure file validation is done
            member_file.clean()
            # Save the MemberFiles object
            member_file.save()
            # Close the file stream
            fp.close()
            # Validate that the file actually exists
            self.assertTrue(MemberFiles.objects.filter(fileName=member_file.fileName) != 0)

    # Test 5: Test that user cannot upload a file with an invalid file extension
    def test_user_cannot_upload_file_w_invalid_file_extension(self):
        with self.assertRaisesRegexp(ValidationError, "Invalid File Extension."):
            # Create a new MemberFiles object
            member_file = MemberFiles()
            # Open the invalid file
            fp = open(self.path_invalidFile, "r")
            # Associate the MF with the file we created
            member_file.fileName = File(fp)
            member_file.relatedMember = self.person1
            # Call the clean() method to ensure file validation is done
            member_file.full_clean()
            # Save the MemberFiles object
            member_file.save()
            # Close the file stream
            fp.close()
    # TODO: David needs to check in the AT document, so we can fix this test criterion.
    # Test 6: Test that a user CANNOT upload an empty file (0B), as these are useless entries to the DB:
    def test_user_can_upload_empty_file(self):
        with self.assertRaisesRegexp(ValidationError, "The submitted file is empty."):
            # Create a new instance of MemberFiles to associate the File to
            member_file = MemberFiles()
            # Open a regular sized file, since this is a valid file test:
            fp = open(self.path_emptyFile, "r")
            # Associate the MemberFile with the File we just opened:
            member_file.fileName = File(fp)
            # Associate the MemberFile with a Member, since MF is a join:
            member_file.relatedMember = self.person1
            # Call the clean method of the model, to do file validation:
            member_file.clean()
            # Save the MemberFile object
            member_file.save()
            # close the file stream
            fp.close()

    # Test 7: Test that a user can upload multiple files to a member:
    # NOTE: simultaneous uploads are not accepted and will crash.
    def test_user_can_upload_more_than_one_file_to_each_member(self):
        # Create new instances of MemberFiles, to associate the files to
        member_file = MemberFiles()
        second_file = MemberFiles()
        # Open two regular sized files:
        fp = open(self.path_midsizedFile, "r")
        f2 = open(self.path_smallFile, "r")
        # Associate the MemberFile with the File we just opened:
        member_file.fileName = File(fp)
        second_file.fileName = File(f2)
        # Associate the MemberFile with a Member, since MF is a join:
        member_file.relatedMember = self.person1
        second_file.relatedMember = self.person1
        # Call the clean method of the model, to do file validation:
        member_file.clean()
        second_file.clean()
        # Save the MemberFile object
        member_file.save()
        second_file.save()
        # close the file stream
        fp.close()
        # Assert that the file exists, meaning our test passes
        self.assertTrue(MemberFiles.objects.filter(fileName=member_file.fileName) != 0 and MemberFiles.objects.filter(
            fileName=second_file.fileName) != 0)

    # Test 8: Test that the database tracks the date when the file is uploaded, in the format DD/MM/YYYY
    def test_database_tracks_file_upload_date(self):
        # Create an instance of MemberFiles
        member_file = MemberFiles()
        # Open a file
        fp = open(self.path_midsizedFile, "r")
        # Associate the MemberFile to the opened file
        member_file.fileName = File(fp)
        # Save the file
        member_file.clean()
        member_file.save()
        # Close the file stream
        fp.close()
        # Assert that the file exists, meaning our test passes
        self.assertTrue(MemberFiles.objects.filter(fileName=member_file.fileName) != 0 and member_file.dateUploaded
                        is not None)

    # Tear down and trash all the old files
    def tearDown(self):
        if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
            shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])
