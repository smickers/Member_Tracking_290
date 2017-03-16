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

    def test_user_can_upload_document_of_valid_file_size_to_member(self):
        # Create new instance of MeetingFiles to associate the File to
        meeting_file = MeetingFiles()
        # Open a regular sized file, since this is a valid test
        fp = open(self.path_midsizedFile, "r")
        # Associate the MeetingFile to the open file
        meeting_file.filename = File(fp)
        # Associate the MeetingFile to the Meeting
        meeting_file.relatedMeeting = self.meeting
        # Call the clean method of the model, to do a file validation
        meeting_file.clean()
        # Save the meeting file object
        meeting_file.save()
        # Close the file stream
        fp.close()
        # Assert that the file exists
        self.assertTrue(MeetingFiles.objects.filter(filename=meeting_file.filename) !=0 )