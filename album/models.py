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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='audio_files')
    title = models.CharField(max_length=60, verbose_name='название песни')
    slug = models.SlugField(max_length=30, unique=True, primary_key=True, blank=True)
    image = models.ImageField(upload_to='image', default='image/default_music_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000, blank=True)
    audio_file = models.FileField(upload_to='audio')
    # duration = models.DurationField()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    image = models.ImageField(upload_to='image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    audio_files = models.ManyToManyField(AudioFile, blank=False)

    def __str__(self):
        return f'{self.author} добавил в альбомы: {self.title}'

# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.utils import timezone
# from pydub import AudioSegment

# @receiver(pre_save, sender=AudioFile)
# def calculate_audio_duration(sender, instance, **kwargs):
#     if not instance.duration and instance.audio_file:
#         audio_file = AudioSegment.from_file(instance.audio_file.path)
#         duration = len(audio_file) / 1000
#         instance.duration = duration
