from rest_framework.routers import DefaultRouter

from . import api_views


alliance_router = DefaultRouter()
alliance_router.register(r'', api_views.AllianceViewSet)
