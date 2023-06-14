from rest_framework import serializers
from .models import AudioFile, Category, Album
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

    

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'image', 'created_at', 'audio_files')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        album = Album.objects.create(author=user, **validated_data)
        return album

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        representation['rating_avg'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        return representation