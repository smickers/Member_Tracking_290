from rest_framework import serializers
from .models import Case


class CaseSearchSerializer(serializers.ModelSerializer):
    """
    Returns serialized form of the indexed fields
    """
    class Meta:
        model = Case
        fields = '__all__'
