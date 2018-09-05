from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Country
from .serializers import CountrySerializers


class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()  # 全て取得
    serializer_class = CountrySerializers
