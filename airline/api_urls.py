from rest_framework.routers import DefaultRouter

from . import api_views


airline_router = DefaultRouter()
airline_router.register(r'', api_views.AirlineViewSet)
