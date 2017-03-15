from drf_haystack.serializers import HaystackSerializer
from search_indexes import CasesIndex

class CaseSearchSerializer(HaystackSerializer):
    """
    Returns serialized form of the indexed fields
    """
    class Meta:
        #Specifify which model classes are your index based on
        index_classes = [CasesIndex]
        #Specify which fields from the index needs to be serialized
        fields = ['text', 'id', 'auto_complete', 'k']
        ignore_fields = ["auto_complete"]

        field_aliases = {
            'q': 'auto_complete'
        }
