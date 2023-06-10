from rest_framework import serializers
from .models import AudioFile, Category, Album, AlbumItem
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AudioFileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = AudioFile
        exclude = ('author',)

    def validate_title(self, title):
        if AudioFile.objects.filter(title=title).exists():
            raise serializers.ValidationError(
                'Пост с таким заголовком уже существует'
            )
        return title
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        audio_file = AudioFile.objects.create(author=user, **validated_data)
        return audio_file
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        representation['comments'] = [i.body for i in instance.comments.all()]
        representation['rating_avg'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        return representation


class AlbumItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumItem
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    # items = AlbumItemSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        album = Album.objects.create(author=user, **validated_data)
        return album
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['album_items'] = AlbumItemSerializer(instance.album_items.all(), many=True).data
        return representation