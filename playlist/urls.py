from django.urls import path, include
from .views import PlaylistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('playlists', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
]