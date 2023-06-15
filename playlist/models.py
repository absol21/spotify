from django.db import models
from django.contrib.auth import get_user_model
from album.models import AudioFile

User = get_user_model()

class Playlist(models.Model):
    title = models.CharField(max_length=70, unique=True)
    artist = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    audio_files = models.ForeignKey(AudioFile, on_delete=models.CASCADE, related_name='playlists', blank=True)

    def __str__(self):
        return f'{self.author} добавил в альбомы: {self.title}'
