from django.core.files.uploadhandler import TemporaryFileUploadHandler, FileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile, StopFutureHandlers
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError
from spfa_mt import settings

class ValidateUploadSize(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(ValidateUploadSize, self).__init__(*args, **kwargs)
        self.total_size = None



    def receive_data_chunk(self, raw_data, start):
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)





    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        super(ValidateUploadSize, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
        print(content_length)
        if content_length > MAX_FILE_SIZE:
            raise ValidationError('Upload size limit exceeded exception')


    def new_file(self, *args, **kwargs):
        super(ValidateUploadSize, self).new_file(*args, **kwargs)
        f_name = self.file_name
        if (f_name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT):
            raise StopFutureHandlers("File type is not allowed")
