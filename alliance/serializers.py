from rest_framework import serializers

from .models import Alliance


class AllianceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alliance
        fields = (
            'id',
            'name_ja',
            'name_en',
        )
