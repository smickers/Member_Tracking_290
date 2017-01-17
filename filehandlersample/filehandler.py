from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.cache import cache

class PercentUpload(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super(PercentUpload, self).__init__(*args, **kwargs)
        self.cache_key = 'Skey'
        cache.set(
            self.cache_key, { 'received': 0}
        )

    def new_file(self, *args, **kwargs):
        super(PercentUpload, self).new_file(*args, **kwargs)
        data = cache.get(self.cache_key, {})


    def receive_data_chunk(self, raw_data, start):
        super(PercentUpload, self).receive_data_chunk(raw_data, start)

        data = cache.get(self.cache_key, {})
        data['received'] += self.chunk_size
        print(data['received'])
        cache.set(
            self.cache_key, data,
        )

