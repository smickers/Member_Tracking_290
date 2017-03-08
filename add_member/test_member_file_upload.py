from .models import Person, MemberFiles
from django.core.files import File
from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ValidationError
from spfa_mt import settings
from datetime import datetime
import shutil
import os.path

"""
Class: MemberFile_UploadTest
This class is for testing file uploads for a member
"""

@override_settings(MEDIA_ROOT='test/')
class MemberFile_UploadTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(MemberFile_UploadTest, cls).setUpClass()

    #Function: init
    #Purpose: This function is used to initialize the variables used for the tests

    def __init__(self, *args, *kwargs):
        super(MemberFile_UploadTest, self).__init__(*args, **kwargs)
        self.CONST.FILE.PATH = settings.STATIC_ROOT + 'add_member/test_file_upload_docs/%s'
        self.MemberFile = MemberFiles()

        self.path_largeFile = self.CONST_FILE_PATH % 'over500MB.txt'
        self.path_midsizedFile = self.CONST_FILE_PATH % 'midSizedFile.txt'
        self.path_smallFile = self.CONST_FILE_PATH % 'smallFile.txt'
        self.path_testFile = self.CONST_FILE_PATH % 'test.txt'
        self.path_picturefile = self.CONST_FILE_PATH % 'picture.jpg'
        self.path_excelFile = self.CONST_FILE_PATH % 'excelFile.jpg'
        self.path_emptyFile = self.CONST_FILE_PATH % 'emptyFile.txt'

    #Function: setUp
    #Purpose: Used to set up testing for a filoe upload
    def setUp(self):
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

        f = open(self.path_testFile, "wb")
        f.seek(30000)
        f.write("\0")
        f.close()

        f = open(self.path_picturefile, "wb")
        f.seek(3000)
        f.close()

        f = open(self.path_excelFile, "wb")
        f.seek(300)
        f.write("\0")
        f.close()

        f = open(self.path_)

