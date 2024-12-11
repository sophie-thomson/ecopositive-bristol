from django.db import IntegrityError
from rest_framework import serializers
from .models import Endorsement


class EndorsementSerializer(serializers.ModelSerializer):
    """
    Serializer for the Endorsement model
    Create method handles the unique constraint on 'owner' and 'endorsed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    endorsed_name = serializers.ReadOnlyField(source='endorsed.name')

    class Meta:
        model = Endorsement
        fields = [
            'id',
            'owner',
            'endorsed',
            'endorsed_name',
            'company',
            'created_on',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
