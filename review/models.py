from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Автор')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.rating


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.post} liked by {self.author.email}'
 

class Playlist(models.Model):
    title  = models.CharField(max_length=200,unique=True)
    post = models.ForeignKey(Post,on_delete=models.DO_NOTHING,related_name='playlists')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    image = models.ImageField(upload_to='image')
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.author} add to playlist {self.title}'
    

