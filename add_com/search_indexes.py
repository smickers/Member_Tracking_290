from haystack import indexes
from meeting.models import Committee

# This class creates the index for each case.
class CommitteeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(use_template=True, indexed=False)
    auto_complete = indexes.EdgeNgramField(index_fieldname='text')

    # Returns the person.
    def get_model(self):
        return CommitteeIndex
