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
    alliance = serializers.SerializerMethodField()

    class Meta:
        model = Lounge
        fields = (
            'id',
            'name_flag',
            'name_ja',
            'name_en',
            'airport',
            'airline',
            'alliance',
            'main_image',
        )

    def get_airport(self, obj):
        airport_abstruct = AirportSerializers(Airport.objects.get(name_ja=obj.airport)).data
        return airport_abstruct

    def get_airline(self, obj):
        airline_abstruct = AirlineSerializers(Airline.objects.get(name_ja=obj.airline)).data
        return airline_abstruct

    def get_alliance(self, obj):
        try:
            alliance_abstruct = AllianceSerializers(Alliance.objects.get(id=obj.airline.member_alliance_id)).data
            return alliance_abstruct
        except:
            alliance_abstruct = None
            return alliance_abstruct

    def get_main_image(self, obj):
        return str('/{a}'.format(a=obj.main_image))