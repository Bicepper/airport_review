from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Alliance
from .serializers import AllianceSerializers


class AllianceViewSet(ReadOnlyModelViewSet):
    queryset = Alliance.objects.all()  # 全て取得
    serializer_class = AllianceSerializers
