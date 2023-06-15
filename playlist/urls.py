from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet

router = DefaultRouter()

router.register('albums', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
]

