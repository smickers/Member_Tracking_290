from drf_haystack.serializers import HaystackSerializer
from add_member.search_indexes import MembersIndex
from rest_framework import serializers
from models import Person

class MemberSearchSerializer(HaystackSerializer):
    """
    Returns serialized form of the indexed fields
    """
    class Meta:
        #Specifify which model classes are your index based on
        index_classes = [MembersIndex]
        #Specify which fields from the index needs to be serialized
        fields = ['text', 'id', 'auto_complete', 'k']
        ignore_fields = ["auto_complete"]

        field_aliases = {
            'q': 'auto_complete'
        }


class MemberFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # index_classes = [MembersIndex]
        fields = '__all__'
