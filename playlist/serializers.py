from rest_framework import serializers
from .models import Playlist
from django.db.models import Avg


class PlaylistSerializer(serializers.ModelSerializer):
    # audio_files = AudioFileSerializer(many=True)

    class Meta:
        model = Playlist
        # fields = ('title', 'image', 'created_at', 'audio_files', 'artist')
        exclude = ('author',)

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        playlist = Playlist.objects.create(author=user, **validated_data)
        return playlist


