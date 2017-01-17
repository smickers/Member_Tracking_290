from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.cache import cache
from spfa_mt.settings import MAX_FILE_SIZE
from django.core.files.uploadhandler import StopUpload


class ValidateUploadSize(TemporaryFileUploadHandler):
    def new_file(self, *args, **kwargs):
        super(ValidateUploadSize, self).new_file(*args, **kwargs)
    
    def receive_data_chunk(self, raw_data, start):
        super(ValidateUploadSize, self).receive_data_chunk(raw_data, start)
        print(self.content_length)
        if(self.content_length > MAX_FILE_SIZE):
            raise StopUpload
