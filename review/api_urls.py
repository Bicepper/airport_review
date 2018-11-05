from rest_framework.routers import DefaultRouter

from .import api_views


review_router = DefaultRouter()
review_router.register(r'', api_views.ReviewViewSet)