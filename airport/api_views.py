from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Airport
from .serializers import AirportSerializers


class AirportViewSet(ReadOnlyModelViewSet):
    queryset = Airport.objects.all()  # 全て取得
    serializer_class = AirportSerializers
