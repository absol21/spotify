# Generated by Django 4.2.1 on 2023-06-10 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=30, unique=True, verbose_name='категории')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('title', models.CharField(max_length=60, verbose_name='название песни')),
                ('slug', models.SlugField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='image/default_music_image.jpg', upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(blank=True, max_length=10000)),
                ('audio_file', models.FileField(upload_to='audio')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_files', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_files', to='album.category')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('description', models.TextField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_items', to='album.album')),
                ('audio_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.audiofile')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='audio_files',
            field=models.ManyToManyField(through='album.AlbumItem', to='album.audiofile'),
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]
