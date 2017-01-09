from haystack import indexes
from .models import Person

# This class creates the index for each member.
class MembersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(use_template=True, indexed=False)

    # Returns the person.
    def get_model(self):
        return Person
