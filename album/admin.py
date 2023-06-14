from django.contrib import admin
from .models import Category, AudioFile, Album


admin.site.register(Category)

class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'audio_file', 'image')
    search_fields = ['title']
    ordering = ['created_at']
    list_filter = ['category__title']

admin.site.register(AudioFile, AudioFileAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'get_rating', 'get_likes')
    search_fields = ['title']
    ordering = ['created_at']

    def get_rating(self, obj):
        from django.db.models import Avg
        result = obj.ratings.aggregate(Avg('rating'))
        return result['rating__avg']

    def get_likes(self, obj):
        result = obj.likes.count()
        return result

admin.site.register(Album, AlbumAdmin)
