from rest_framework import serializers

from . models import Airline


class AirlineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = (
            'id',
            'name_ja',
            'name_en',
            'member_alliance_id',
        )
