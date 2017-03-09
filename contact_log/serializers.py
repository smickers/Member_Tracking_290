from models import contactLog
from rest_framework import serializers

class ContactLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contactLog
        fields = ('member', 'date', 'description', 'contactCode')