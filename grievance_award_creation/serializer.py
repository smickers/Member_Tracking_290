from rest_framework import serializers
from models import GrievanceAward


class GAFilterSerializer(serializers.ModelSerializer):
    """
    Serializes our member/person with all fields.
    """
    class Meta:
        model = GrievanceAward
        fields = '__all__'