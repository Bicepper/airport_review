from rest_framework.routers import DefaultRouter

from .import api_views


airport_router = DefaultRouter()
airport_router.register(r'', api_views.AirportViewSet)
