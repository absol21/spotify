from django.contrib import admin
from .models import Category, Post


admin.site.register(Category)
# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'audio_file', 'image')
    search_fields = ['title']
    ordering = ['created_at']
    list_filter = ['category__title']

admin.site.register(Post, PostAdmin)
