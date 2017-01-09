from drf_haystack.serializers import HaystackSerializer
from add_member.search_indexes import MembersIndex

class MemberSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [MembersIndex]
        fields = ['text', 'id']
