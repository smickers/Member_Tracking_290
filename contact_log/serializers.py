# Cameron Auser
# SPFA MT Project
# March 20, 2017
from models import contactLog
from rest_framework import serializers

# Class:    ContactLogSerializer
# Purpose:  Define serialization options for a contact log.
class ContactLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactLog
        # What fields should be serialized
        fields = ('id', 'member', 'date', 'description', 'contactCode')
        # How many levels of foreign keys should be serialized before we just
        # serialize the ID itself? I'm doing one level here so that the member's
        # name is serialized.
        depth = 1