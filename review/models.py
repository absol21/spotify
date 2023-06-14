from django.db import models
from django.contrib.auth import get_user_model
from album.models import Album

User = get_user_model()


class Rating(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='ratings', verbose_name='album')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Автор')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.rating


class Like(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.album} liked by {self.author.email}'
 
