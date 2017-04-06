from rest_framework import serializers
from models import GrievanceAward


class GAFilterSerializer(serializers.ModelSerializer):
    """
    Serializes our member/person with all fields.
    """
    class Meta:
        model = GrievanceAward
        fields = '__all__'


# Class:    GrievanceAwardSerializer
# Purpose:  Define serialization options for a grievance award.
class GrievanceAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievanceAward
        # What fields should be serialized
        fields = '__all__'
