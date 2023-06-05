# Generated by Django 4.2.1 on 2023-06-05 14:10

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
            name='Category',
            fields=[
                ('title', models.CharField(max_length=30, unique=True, verbose_name='категории')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=60, verbose_name='название песни')),
                ('slug', models.SlugField(blank=True, max_length=120, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(blank=True, max_length=10000)),
                ('audio_file', models.FileField(upload_to='audio')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.category', verbose_name='категории')),
            ],
        ),
    ]
