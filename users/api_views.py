from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import User
from .serializers import UserSerializers


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
