from rest_framework import serializers
from .models import Case


class CaseSearchSerializer(serializers.ModelSerializer):
    """
    Returns serialized form of the indexed fields
    """
    class Meta:
        model = Case
        fields = '__all__'
        ignore_fields = ["auto_complete"]
        field_aliases = {
            'q': 'auto_complete'
        }


class CaseFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'
        depth = 1