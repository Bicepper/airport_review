from rest_framework import serializers

from .models import Airport


class AirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            'id',
            'name_ja',
            'name_en',
            'coordinate_latitude',
            'coordinate_longitude',
            'main_image',
            'country_id',
        )
