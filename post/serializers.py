from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title):
        if Post.objects.filter(title=title).exists():
            raise serializers.ValidationError(
                'Пост с таким заголовком уже существует'
            )
        return title
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        post = Post.objects.create(author=user, **validated_data)
        return post
    
    