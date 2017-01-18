from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile, FileUploadHandler
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError

class ValidateUploadSize(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(ValidateUploadSize, self).__init__(*args, **kwargs)
        self.total_size = 0


    def receive_data_chunk(self, raw_data, start):
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)
        #print(self.total_size)
        self.total_size += len(raw_data)
        if self.total_size > MAX_FILE_SIZE:
            #raise ValidationError('Upload size limit exceeded exception')
            raise StopUpload(connection_reset=True)
        return raw_data


    # def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
    #     super(ValidateUploadSize, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
    #     self.total_size = content_length

    def file_complete(self, file_size):
        return None

class CustomUploadError(Exception):
    pass

# class CancelUpload(TemporaryFileUploadHandler):
#     def receive_data_chunk(self, raw_data, start):
#         super(CancelUpload, self).receive_data_chunk(raw_data, start)
#         raise SkipFile

class ErroringUploadHandler(FileUploadHandler):
    def receive_data_chunk(self, raw_data, start):
        raise CustomUploadError("File exceeded limit of 500mb")