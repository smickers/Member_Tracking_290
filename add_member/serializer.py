from drf_haystack.serializers import HaystackSerializer
from add_member.search_indexes import MembersIndex
from rest_framework import serializers
from add_member.models import PersonFile, Person


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


class MemberFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonFile
        fields = ['file', 'id']

    def validate(self, attrs):
        instance = PersonFile(**attrs)
        instance.clean()
        return attrs
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' 
    
    def validate(self, attrs): 
        instance = Person(**attrs)
        instance.clean()
        return attrs
    
