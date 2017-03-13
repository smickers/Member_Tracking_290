from models import contactLog
from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer
from contact_log.search_indexes import ContactLogIndex
from add_member.serializer import MemberSearchSerializer

#class ContactLogSerializer(HaystackSerializer):

# class ContactLogSerializer(serializers.HyperlinkedModelSerializer):
#     member = MemberSearchSerializer()
#     class Meta:
#         #index_classes = [ContactLogIndex]
#         model = contactLog
#         #fields = ['text', 'id', 'auto_complete', 'k']
#         fields = ( 'member', 'date', 'description', 'contactCode')
#         #ignore_fields = ["auto_complete"]
#
#         #field_aliases = {
#         #    'q': 'auto_complete'
#         #}


class ContactLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactLog
        fields = ('id', 'member', 'date', 'description', 'contactCode')
        depth = 1