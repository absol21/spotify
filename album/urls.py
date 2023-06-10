from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AlbumViewSet, AudioFileViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('albums', AlbumViewSet)
router.register('audio_file', AudioFileViewSet)

urlpatterns = [
    path('', include(router.urls))
]

