from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Review
from .serializers import ReviewSerializers


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = Review.objects.all()  # 全て取得
    serializer_class = ReviewSerializers