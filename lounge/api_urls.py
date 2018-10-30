from rest_framework.routers import DefaultRouter

from .import api_views


lounge_router = DefaultRouter()
lounge_router.register(r'', api_views.LoungeViewSet)