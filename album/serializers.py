from rest_framework import serializers
from .models import AudioFile, Category, Album
from django.db.models import Avg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AudioFileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, allow_null=False)

    class Meta:
        model = AudioFile
        exclude = ('author',)


    def validate_image(self, image):
        if image.size > 4 * 1024 * 1024:
            raise serializers.ValidationError(
                'Изображение слишком большое'
                )
        return image

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        audio_file = AudioFile.objects.create(author=user, **validated_data)
        return audio_file


class AlbumSerializer(serializers.ModelSerializer):
    # audio_files = AudioFileSerializer(many=True)

    class Meta:
        model = Album
        # fields = ('title', 'image', 'created_at', 'audio_files', 'artist')
        exclude = ('author',)

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
