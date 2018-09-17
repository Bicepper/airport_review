from rest_framework import serializers

from .models import Airport


class AirportSerializers(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()

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

    def get_main_image(self, obj):
        return str('/{a}'.format(a=obj.main_image))

