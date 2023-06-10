from django.contrib import admin
from .models import Category, AudioFile, AlbumItem, Album


admin.site.register(Category)


from django.contrib import admin
from .models import AudioFile, AlbumItem, Album


class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'audio_file', 'image')
    search_fields = ['title']
    ordering = ['created_at']
    list_filter = ['category__title']

admin.site.register(AudioFile, AudioFileAdmin)


class AlbumItemAdmin(admin.ModelAdmin):
    list_display = ('album', 'position', 'image')
    search_fields = ['album__title']
    ordering = ['position']

admin.site.register(AlbumItem, AlbumItemAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
    search_fields = ['title']
    ordering = ['created_at']

admin.site.register(Album, AlbumAdmin)
