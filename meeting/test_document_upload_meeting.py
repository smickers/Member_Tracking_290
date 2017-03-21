from .models import Meeting, MeetingFiles, Committee, Person
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
class MeetingFileUploadTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MeetingFileUploadTest, cls).setUpClass()

    # Function: init
    # Purpose: This function is used to initialize the variables used for the tests
    def __init__(self, *args, **kwargs):
        super(MeetingFileUploadTest, self).__init__(*args, **kwargs)
        # Feels cheap, but why create more bloat in the application? Use what they
        # made back in grievance award file uploads.
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'grievance_award_creation/test_files_grievance_docs_upload/%s'
        self.meeting = Meeting()
        self.MeetingFile = MeetingFiles()
        self.path_largeFile = self.CONST_FILE_PATH % 'dummylarge.txt'
        self.path_midsizedFile = self.CONST_FILE_PATH % 'notsolarge.txt'
        self.path_smallFile = self.CONST_FILE_PATH % 'SmallFile.txt'
        self.path_invalidFile = self.CONST_FILE_PATH % 'invalid.exe'
        self.path_emptyFile = self.CONST_FILE_PATH % 'emptyFile.txt'

    # Function: setUp
    # Purpose: Used to set up all the models need for uploading file to a meeting
    def setUp(self):
        committee = Committee()
        committee.name = "Finance"
        committee.status = 1
        committee.full_clean()
        committee.save()

        person = Person()
        person.memberID = 4204444
        person.firstName = 'First'
        person.middleName = 'Middle'
        person.lastName = 'Last'
        person.socNum = 123456789
        person.city = 'Sample City'
        person.mailAddress = 'Sample address'
        person.mailAddress2 = 'Sample Address 2'
        person.pCode = 's7k5j8'
        person.hPhone = '(306)812-1234'
        person.cPhone = '(306)812-1234'
        person.hEmail = 'sample@sample.com'
        person.campus = 'SASKATOON'
        person.jobType = 'FTO'
        person.committee = 'Sample Committee'
        person.memberImage = 'image.img'
        person.bDay = '2012-03-03'
        person.hireDate = '2012-03-03'
        person.gender = 'MALE'
        person.membershipStatus = 'RESOURCE'
        person.programChoice = 'Sample Program'
        person.full_clean()
        person.save()

        self.meeting = Meeting()
        self.meeting.committee = committee
        self.meeting.liaison = '1234'
        self.meeting.date = "2016-10-20"
        self.meeting.description = 'a' * 500
        self.meeting.full_clean()
        self.meeting.save()

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

    # This test tests that a file can be uploaded also test file size under 500mb
    def test_user_can_upload_document_of_valid_file_size_to_member(self):
        # Create new instance of MeetingFiles to associate the File to
        meeting_file = MeetingFiles()
        # Open a regular sized file, since this is a valid test
        fp = open(self.path_midsizedFile, "r")
        # Associate the MeetingFile to the open file
        meeting_file.fileName = File(fp)
        # Associate the MeetingFile to the Meeting
        meeting_file.relatedMeeting = self.meeting
        # Call the clean method of the model, to do a file validation
        meeting_file.clean()
        # Save the meeting file object
        meeting_file.save()
        # Close the file stream
        fp.close()
        # Assert that the file exists
        self.assertTrue(MeetingFiles.objects.filter(fileName=meeting_file.fileName) !=0 )

    # This test tests that a file larger than 500mb cannot be uploaded
    def test_user_cannot_upload_oversize_file_to_meeting(self):
        with self.assertRaisesRegexp(ValidationError, "Upload size limit exceeded exception"):
            # Create a new instance of MemberFiles to associate the File to
            meeting_file = MeetingFiles()
            # Open a regular sized file, since this is a valid test
            fp = open(self.path_largeFile, "r")
            # Associate the MeetingFile with the file we just opened
            meeting_file.fileName = File(fp)
            # Associate the MeetingFile to the Meeting
            meeting_file.relatedMeeting = self.meeting
            # Clean the file
            meeting_file.clean()
            # Save the file (attempt)
            meeting_file.save()
            # Close the stream
            fp.close()

            # Assert the file exists
            self.assertTrue(MeetingFiles.objects.filter(fileName = meeting_file.fileName) != 0)

    # This test tests that a proper file extensions  can be uploaded
    def test_user_can_upload_file_with_valid_file_exension(self):
        acceptedExtensions = settings.FILE_EXT_TO_ACCEPT

        for ext in acceptedExtensions:
            # Create a file name for each exension in the list
            valid_file = "valid_data.%s" % ext
            # Build the file path create the file
            file_path = self.CONST_FILE_PATH % valid_file
            f = open(file_path, "wb")
            f.seek(5)
            f.write("\0")
            f.close()

            # Create a new instance of MemberFiles to associate the File to
            meeting_file = MeetingFiles()
            # Open a regular sized file, since this is a valid test
            fp = open(file_path, "r")
            # Associate the MeetingFile with the file we just opened
            meeting_file.fileName = File(fp)
            # Associate the MeetingFile to the Meeting
            meeting_file.relatedMeeting = self.meeting
            # Clean the file
            meeting_file.clean()
            # Save the file (attempt)
            meeting_file.save()
            # Close the stream
            fp.close()

            # Assert the file exists
            self.assertTrue(MeetingFiles.objects.filter(fileName=meeting_file.fileName) != 0)

    # This test tests that files with invalid extensions cannot be uploaded
    def test_user_cannot_ulpload_file_with_invalid_extension(self):
        with self.assertRaisesRegexp(ValidationError, "Invalid File Extension"):
            # Create a new instance of MemberFiles to associate the File to
            meeting_file = MeetingFiles()
            # Open a regular sized file, since this is a valid test
            fp = open(self.path_invalidFile, "r")
            # Associate the MeetingFile with the file we just opened
            meeting_file.fileName = File(fp)
            # Associate the MeetingFile to the Meeting
            meeting_file.relatedMeeting = self.meeting
            # Clean the file
            meeting_file.clean()
            # Save the file (attempt)
            meeting_file.save()
            # Close the stream
            fp.close()

    # This test tests that an empty file cannot be uploaded
    def test_user_cannot_upload_empty_file(self):
        with self.assertRaisesRegexp(ValidationError, "The submitted file is empty."):
            # Create a new instance of MemberFiles to associate the File to
            meeting_file = MeetingFiles()
            # Open a regular sized file, since this is a valid test
            fp = open(self.path_emptyFile, "r")
            # Associate the MeetingFile with the file we just opened
            meeting_file.fileName = File(fp)
            # Associate the MeetingFile to the Meeting
            meeting_file.relatedMeeting = self.meeting
            # Clean the file
            meeting_file.clean()
            # Save the file (attempt)
            meeting_file.save()
            # Close the stream
            fp.close()

    # This test tests that multiple file can be uploaded to a member
    # Cannot upload more than one at a time
    def test_user_can_upload_more_than_one_file_to_each_meeting(self):
        # Create two new files to associate to a meeting
        # Create a new instance of MemberFiles to associate the File to
        meeting_file = MeetingFiles()
        second_file = MeetingFiles()
        # Open a regular sized file, since this is a valid test
        fp = open(self.path_smallFile, "r")
        f2 = open(self.path_midsizedFile, "r")
        # Associate the MeetingFile with the file we just opened
        meeting_file.fileName = File(fp)
        second_file.fileName = File(f2)
        # Associate the MeetingFile to the Meeting
        meeting_file.relatedMeeting = self.meeting
        second_file.relatedMeeting = self.meeting
        # Clean the file
        meeting_file.clean()
        second_file.clean()
        # Save the file (attempt)
        meeting_file.save()
        second_file.save()
        # Close the stream
        fp.close()

        # Assert that the file exists, meaning our test passes
        self.assertTrue(MeetingFiles.objects.filter(fileName=meeting_file.fileName) != 0
                        and MeetingFiles.objects.filter(fileName=second_file.fileName) != 0)

     # This tests tests that the databse tracks the date the file was uploaded
    def test_database_tracks_file_upload_date(self):
        # Create a new instance of MemberFiles to associate the File to
        meeting_file = MeetingFiles()
        # Open a regular sized file, since this is a valid test
        fp = open(self.path_smallFile, "r")
        # Associate the MeetingFile with the file we just opened
        meeting_file.fileName = File(fp)
        # Associate the MeetingFile to the Meeting
        meeting_file.relatedMeeting = self.meeting
        # Clean the file
        meeting_file.clean()
        # Save the file (attempt)
        meeting_file.save()
        # Close the stream
        fp.close()

        # Assert that the file exists, meaning our test passes
        self.assertTrue(MeetingFiles.objects.filter(fileName=meeting_file.fileName) != 0
                        and meeting_file.dateUploaded is not None)

    # Tear down and trash all the old files
    def tearDown(self):
        if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
            shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])