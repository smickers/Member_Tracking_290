from django.core.files.uploadhandler import TemporaryFileUploadHandler, FileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile, StopFutureHandlers
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from spfa_mt import settings
from rest_framework.exceptions import APIException
"""
Class UploadValidator
This class handles validating uploads for the entire website
TemporaryFileUploadHandler is a class used by Django and can overwritten to define custom handlers
File extensions and the max size of a file are included in the settings
"""
class UploadValidator(TemporaryFileUploadHandler):
    """
    Method: init
    Purpose: Class constructor
    """
    def __init__(self, *args, **kwargs):
        super(UploadValidator, self).__init__(*args, **kwargs)
        self.total_size = None

    """
    Method: file_complete
    Purpose: This method is run after a file has been uploaded. The file's size is
    passed to this method, so we're using this method to validate that a file is
    small enough to be stored in the system.

    THIS CHECK USED TO BE DONE IN receive_data_chunk. However, I moved it here because
    raising an exception in receive_data_chunk would give Connection Reset errors in the
    browser. By raising the validation in this method, we can display a nice error on the
    screen after the user has uploaded the file, rather than giving connection reset errors
    with no debug information as soon as the upload begins.
    """
    def file_complete(self, file_size):
        if file_size > MAX_FILE_SIZE:
            print("File_complete running!")
            raise FileTooLarge
        return super(UploadValidator, self).file_complete(file_size)

    """
    Method: handle_raw_input
    Purpose: Allows the handler to completely override the parsing of the raw HTTP input.
    """
    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        super(UploadValidator, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
        self.total_size = content_length
        if self.total_size > MAX_FILE_SIZE:
            raise FileTooLarge

    """
    Method: new_file
    Purpose: Callback signaling that a new file upload is starting.
             This is called before any data has been fed to any upload handlers.
    """
    def new_file(self, *args, **kwargs):
        super(UploadValidator, self).new_file(*args, **kwargs)
        f_name = self.file_name
        if (f_name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT):
            """
                Raises exception if the file extension is invalid
            """

            raise StopFutureHandlers("File type is not allowed")


class FileTooLarge(APIException, StopFutureHandlers):
    """
        This exceptions gets raised if the file uploaded is exceeding the file size limit
    """
    status_code = 400
    default_detail = 'The file exceeded the file size limit. Please upload a smaller file'
    default_code = 'bad request'

