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
        super().save()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name='категории')
    title = models.CharField(max_length=60, verbose_name='название песни')
    slug = models.SlugField(max_length=120, blank=True, primary_key=True)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000, blank=True)
    audio_file = models.FileField(upload_to='audio')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *arg, **kwargs) -> slug:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

