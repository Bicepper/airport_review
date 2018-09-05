from rest_framework import serializers

from .models import Country


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'name_ja',
            'name_en',
        )