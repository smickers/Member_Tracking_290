from django.core.files.uploadhandler import TemporaryFileUploadHandler, FileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile, StopFutureHandlers
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError

class ValidateUploadSize(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(ValidateUploadSize, self).__init__(*args, **kwargs)
        self.total_size = None


    def receive_data_chunk(self, raw_data, start):
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)
        if self.total_size > MAX_FILE_SIZE:
            raise ValidationError('Upload size limit exceeded exception')



    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        super(ValidateUploadSize, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
        self.total_size = content_length



class CancelUpload(FileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(CancelUpload, self).__init__(*args, **kwargs)
        raise SkipFile()

    def new_file(self, field_name, file_name, content_type, content_length, charset=None, content_type_extra=None):
        super(CancelUpload, self).new_file(file_name, content_type, content_length, charset=None, content_type_extra=None)
        print('future')
        raise StopFutureHandlers()



    # def receive_data_chunk(self, raw_data, start):
    #     print('hi')
    #     super(CancelUpload, self).receive_data_chunk(raw_data, start)
    #     raise StopFutureHandlers
