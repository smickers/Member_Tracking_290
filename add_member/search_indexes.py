from haystack import indexes
from .models import Person

class MembersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Person