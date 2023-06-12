from rest_framework import serializers
from .models import Playlist
from django.db.models import Avg


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title', 'image', 'created_at', 'description', 'audio_files')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        audio_files = validated_data.pop('audio_files', [])
        # if not audio_files:
        #     raise serializers.ValidationError(
        #         "Аудиофайл обязателен для создания альбома."
        #         )
        image = validated_data.get('image')
        if not image:
            image = audio_files[0].image
        playlist = Playlist.objects.create(author=user, **validated_data)
        playlist.image = image
        playlist.save()
        # album.audio_files.set(audio_files)
        return playlist