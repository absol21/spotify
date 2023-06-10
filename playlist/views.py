from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from review.views import PermissionMixin
from .serializers import PlaylistSerializer, Playlist

class PlaylistViewSet(PermissionMixin, ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
