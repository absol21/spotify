from django.db import models
from django.contrib.auth import get_user_model
from album.models import AudioFile

User = get_user_model()

class Playlist(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.author} added to playlist: {self.title}'


class PlayListItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='playlist_items')
    audio_file = models.ForeignKey(AudioFile, on_delete=models.CASCADE, related_name='playlist_items')
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.audio_file} in {self.playlist}'