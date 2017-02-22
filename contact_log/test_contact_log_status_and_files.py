# SPFA MT CST Project
from spfa_mt import settings
from django.test import TestCase
from .models import contactLog, ContactLogFile
from add_member.models import Person
from django.core.exceptions import ValidationError
from spfa_mt import kvp
from django.test import override_settings
from django.core.files import File
import os
import shutil


# Make sure we aren't writing crap data to the same location
# as where the real data lives
@override_settings(MEDIA_ROOT='test/')
# Class to test adding a document/file to a contact log
class ContactLogEditTests(TestCase):
    cLog = contactLog()
    person1 = Person()
    person2 = Person()
    person3 = Person()
    # Unit test setup method
    def setUp(self):
        # Set up our people
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

        # Set up the contact log to be edited
        self.cLog.member = self.person1
        self.cLog.date = '2017-02-12'
        self.cLog.description = 'Hello world!'
        self.cLog.contactCode = 'E'
        self.cLog.clean()
        self.cLog.save()

        # Put together some sample files
        # This is nabbing the same test files that were used to test document upload for cases.
        # No need to clog the system with extra test files if they already exist, yeah?
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'add_case/test_case_file_upload/%s'
        self.oversizeFile = self.CONST_FILE_PATH % "COSA190.docx"
        self.undersizeFile = self.CONST_FILE_PATH % "COSC195.docx"
        self.invalidFile = self.CONST_FILE_PATH % "my_C_program.exe"

        # Create a file that exceeds max file size, for testing
        f = open(self.oversizeFile, "wb")
        f.seek(settings.MAX_FILE_SIZE + 1)
        f.write("\0")
        f.close()

        # Create a file that does not exceed max file size, for testing
        f = open(self.undersizeFile, "wb")
        f.seek(settings.MAX_FILE_SIZE - 1)
        f.write("\0")
        f.close()

        # Create a file with an invalid file type, for testing
        f = open(self.invalidFile, "wb")
        f.seek(564)
        f.write("\0")
        f.close()

    # Test 1: Ensure all valid contact codes are accepted
    def test_valid_contact_codes(self):
        # Loop through all the valid status codes, ensure we can save it
        for status in kvp.CONTACT_LOG_STATUSES[0]:
            self.cLog = contactLog()
            self.cLog.member = self.person1
            self.cLog.date = '2017-01-01'
            self.cLog.description = 'Example Entry'
            self.cLog.contactCode = status[0]
            self.cLog.clean()
            self.cLog.save()

    # Test 2: Ensure an invalid contact code is not accepted
    def test_invalid_contact_code(self):
        with self.assertRaisesRegexp(ValidationError, 'Please select an option from the list of choices.'):
            self.cLog.member = self.person1
            self.cLog.date = '2017-01-01'
            self.cLog.description = 'Example Entry'
            self.cLog.contactCode = 'X'
            self.cLog.clean()
            self.cLog.save()

    # Test 3: Ensure all valid file extensions are accepted
    def test_valid_file_extension_are_accepted(self):
        accepted_file_extensions = settings.FILE_EXT_TO_ACCEPT
        for extension in accepted_file_extensions:
            # Create a file name for each extension in the list
            file_name = "important_data.%s" % extension
            # build the file path and create the file
            file_path = self.CONST_FILE_PATH % file_name
            f = open(file_path, "wb")
            f.seek(5)
            f.write("\0")
            f.close()
            # Create a new ContactLogFile object
            contact_log_file = ContactLogFile()
            # Open the actual file
            fp = open(file_path, "r")
            # Associate the ContactLogFile, with a real file
            contact_log_file.fileName = File(fp)
            # Associate ContactLogFile object with a contact log
            contact_log_file.relatedContactLog = self.cLog
            # Call the clean() method to ensure validation
            contact_log_file.clean()
            # Save the Case File object
            contact_log_file.save()
            # close file stream
            fp.close()
            # Validate that this file actually exists
            self.assertTrue(os.path.isfile(file_path))

    # Test 4: Ensure an invalid file extension is rejected
    def test_invalid_file_extension_is_rejected(self):
        with self.assertRaisesRegexp(ValidationError, "Invalid File Extension."):
            # Use the invalidFile we created in setUp
            file_name = self.invalidFile
            # Create a new instance of a ContactLogFile to associate the File to
            contact_log_file = ContactLogFile()
            # Open our oversize file
            fp = open(file_name, "r")
            # Associate the contact log file, with the correctly sized file we opened
            contact_log_file.fileName = File(fp)
            # Associate ContactLogFile object with a contact log (required)
            contact_log_file.relatedContactLog = self.cLog
            # Call the clean method of the model
            contact_log_file.clean()
            # Save the ContactLogFile object
            contact_log_file.save()
            # close file stream
            fp.close()

    # Test 5: Ensure that a file that is less than 500MB can be uploaded.
    def test_ensure_a_lower_than_500mb_file_can_be_uploaded(self):
        # We created an undersizeFile in our setUp method:
        file_name = self.undersizeFile
        # Create a new instance of a ContactLogFile to associate the File to
        contact_log_file = ContactLogFile()
        # Open our oversize file
        fp = open(file_name, "r")
        # Associate the contact log file, with the correctly sized file we opened
        contact_log_file.fileName = File(fp)
        # Associate ContactLogFile object with a contact log (required)
        contact_log_file.relatedContactLog = self.cLog
        # Call the clean method of the model
        contact_log_file.clean()
        # Save the ContactLogFile object
        contact_log_file.save()
        # close file stream
        fp.close()

    # Test 6: Ensure that a file that over 500MB cannot be uploaded.
    def test_ensure_a_file_larger_than_500mb_file_cannot_be_uploaded(self):
        with self.assertRaisesRegexp(ValidationError, "File is too large."):
            # Use the oversized file we created in setUp:
            file_name = self.oversizeFile
            # open our over-sized, exception-throwing file
            fp = open(file_name, "r")
            # Create a new instance of a ContactLogFile to associate the File to
            contact_log_file = ContactLogFile()
            # Associate the contact log file, with the oversized file we opened
            contact_log_file.fileName = File(fp)
            # Associate ContactLogFile object with a contact log
            contact_log_file.relatedContactLog = self.cLog
            # Call the clean method of the model
            contact_log_file.clean()
            # Save the ContactLogFile object
            contact_log_file.save()
            # close file stream
            fp.close()

    # If we created a file, ditch it.
    def tearDown(self):
        if os.path.exists(self._overridden_settings["MEDIA_ROOT"]):
            shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])
