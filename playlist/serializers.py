from rest_framework import serializers
from album.serializers import AudioFileSerializer 
from .models import Playlist, PlayListItem

class PlayListItemSerializer(serializers.ModelSerializer):
    audio_file = AudioFileSerializer()

    class Meta:
        model = PlayListItem
        fields = ['id', 'track', 'position']

class PlaylistSerializer(serializers.ModelSerializer):
    playlist_items = PlayListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'author', 'image', 'created_at', 'description', 'playlist_items']
