from django.contrib import admin
from .models import Rating,Like,Playlist,Comment

admin.site.register(Rating)
admin.site.register(Like)
# admin.site.register(Playlist)
admin.site.register(Comment)



class PlayAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_rating', 'get_likes', 'get_favorites', 'image')
    search_fields = ['title', 'body']
    # ordering = ['']
    list_filter = []

    def get_rating(self, obj):
        from django.db.models import Avg
        result = obj.ratings.aggregate(Avg('rating'))
        return result['rating__avg']

    def get_likes(self, obj):
        result = obj.likes.count()
        return result

    def get_favorites(self, obj):
        result = obj.favorites.count()
        return result

admin.site.register(Playlist, PlayAdmin)
