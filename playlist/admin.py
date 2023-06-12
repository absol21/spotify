from django.contrib import admin
from .models import Playlist 


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
    search_fields = ['title']
    ordering = ['created_at']

admin.site.register(Playlist, PlaylistAdmin)
