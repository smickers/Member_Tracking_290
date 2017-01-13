from haystack import indexes
from .models import Person

# This class creates the index for each member.
class MembersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(use_template=True, indexed=False)
    auto_complete = indexes.EdgeNgramField(index_fieldname='text')

    # Returns the person.
    def get_model(self):
        return Person
