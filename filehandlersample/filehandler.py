from django.core.files.uploadhandler import TemporaryFileUploadHandler, FileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile, StopFutureHandlers
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError
from spfa_mt import settings

class ValidateUploadSize(TemporaryFileUploadHandler):
    """
        Class constructor
    """
    def __init__(self, *args, **kwargs):
        super(ValidateUploadSize, self).__init__(*args, **kwargs)
        self.total_size = None



    def receive_data_chunk(self, raw_data, start):
        """
            Receives a chunk of data from the file upload.
        """
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)
        if self.total_size > MAX_FILE_SIZE:
            """
                Raises exception if the file size is invalid
            """
            raise ValidationError('Upload size limit exceeded exception')

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        """
            Allows the handler to completely override the parsing of the raw HTTP input.
        """
        super(ValidateUploadSize, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
        self.total_size = content_length



    def new_file(self, *args, **kwargs):
        """
            Callback signaling that a new file upload is starting. This is called before any data has been fed to any upload handlers.
        """
        super(ValidateUploadSize, self).new_file(*args, **kwargs)
        f_name = self.file_name
        if (f_name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT):
            """
                Raises exception if the file extension is invalid
            """
            raise StopFutureHandlers("File type is not allowed")
