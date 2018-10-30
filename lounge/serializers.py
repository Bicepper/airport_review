from rest_framework import serializers

from .models import Lounge

from airport.models import Airport
from airport.serializers import AirportSerializers


class LoungeSerializers(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    airport = serializers.SerializerMethodField()

    class Meta:
        model = Lounge
        fields = (
            'id',
            'name_flag',
            'name_ja',
            'name_en',
            'airport',
            'airline',
            'main_image',
        )

    def get_airport(self, obj):
        print('================louneのAPI=================')
        print(obj.airport)
        print('================louneのAPI=================')
        airport_abstruct = AirportSerializers(Airport.objects.all().filter(airport=Airport.objects.get(id=obj.airport)))
        return obj.airport

    def get_main_image(self, obj):
        return str('/{a}'.format(a=obj.main_image))
