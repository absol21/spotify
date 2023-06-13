from django.contrib import admin
from .models import Rating,Like

admin.site.register(Like)


class PlayAdmin(admin.ModelAdmin):
    list_display = ('get_rating', 'get_likes')
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

admin.site.register(Rating ,PlayAdmin)
