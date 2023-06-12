from rest_framework import serializers
from .models import AudioFile, Category, Album
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AudioFileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    duration = serializers.DurationField(read_only=True)
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
    

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'image', 'created_at', 'description', 'audio_files')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        audio_files = validated_data.pop('audio_files', [])
        if not audio_files:
            raise serializers.ValidationError(
                "Аудиофайл обязателен для создания альбома."
                )
        image = validated_data.get('image')
        if not image:
            image = audio_files[0].image
        album = Album.objects.create(author=user, **validated_data)
        album.image = image
        album.save()
        album.audio_files.set(audio_files)
        return album
