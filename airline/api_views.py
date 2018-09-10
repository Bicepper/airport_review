from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Airline
from .serializers import AirlineSerializers


class AirlineViewSet(ReadOnlyModelViewSet):
    queryset = Airline.objects.all()  # 全て取得
    serializer_class = AirlineSerializers
