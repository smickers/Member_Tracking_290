from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.files.uploadhandler import StopUpload, SkipFile
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.exceptions import ValidationError

class ValidateUploadSize(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(ValidateUploadSize, self).__init__(*args, **kwargs)
        self.total_size = None


    def receive_data_chunk(self, raw_data, start):
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)
        print(self.total_size)

        if self.total_size > MAX_FILE_SIZE:
            raise ValidationError('Upload size limit exceeded exception')
            # raise StopUpload(connection_reset=True)


    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        super(ValidateUploadSize, self).handle_raw_input(input_data, META, content_length, boundary, encoding=None)
        self.total_size = content_length


class CancelUpload(TemporaryFileUploadHandler):
    def receive_data_chunk(self, raw_data, start):
        super(CancelUpload, self).receive_data_chunk(raw_data, start)
        raise SkipFile
