from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Lounge
from .serializers import LoungeSerializers


class LoungeViewSet(ReadOnlyModelViewSet):
    queryset = Lounge.objects.all()  # 全て取得
    serializer_class = LoungeSerializers
