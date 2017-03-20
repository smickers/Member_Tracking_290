from haystack import indexes
from .models import contactLog

# This class creates the index for each contact log.
class ContactLogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(use_template=True, indexed=False)
    auto_complete = indexes.EdgeNgramField(index_fieldname='text')

    # Returns the contact log.
    def get_model(self):
        return contactLog
