from rest_framework.routers import DefaultRouter

from . import api_views


country_router = DefaultRouter()
country_router.register(r'', api_views.CountryViewSet)
