from rest_framework import serializers

from .models import Lounge

from airport.models import Airport
from airline.models import Airline
from alliance.models import Alliance
from airport.serializers import AirportSerializers
from airline.serializers import AirlineSerializers
from alliance.serializers import AllianceSerializers


class LoungeSerializers(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    airport = serializers.SerializerMethodField()
    airline = serializers.SerializerMethodField()

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
        airport_abstruct = AirportSerializers(Airport.objects.get(name_ja=obj.airport)).data
        return airport_abstruct

    def get_airline(self, obj):
        airline_abstruct = AirlineSerializers(Airline.objects.all().get(name_ja=obj.airline)).data
        # alliance_abstruct = AllianceSerializers(Alliance.objects.get(id=airline_abstruct['id'])).data
        return airline_abstruct

    def get_main_image(self, obj):
        return str('/{a}'.format(a=obj.main_image))