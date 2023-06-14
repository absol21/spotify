from django.db import models
from slugify import slugify 
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='категории')
    slug = models.SlugField(max_length=30, unique=True, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *arg, **kwargs) -> slug:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)


class AudioFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_files')
    artist = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='audio_files')
    title = models.CharField(max_length=60, verbose_name='название песни')
    slug = models.SlugField(max_length=30, unique=True, primary_key=True, blank=True)
    image = models.ImageField(upload_to='image', default='image/default_music_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to='audio')


    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=70, unique=True)
    artist = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    audio_files = models.ForeignKey(AudioFile, on_delete=models.CASCADE, related_name='albums', blank=True)

    def __str__(self):
        return f'{self.author} добавил в альбомы: {self.title}'