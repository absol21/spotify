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


# class AlbumSerializer(serializers.ModelSerializer):
#     # audio_files = AudioFileSerializer(many=True)

#     class Meta:
#         model = Album
#         # fields = ('title', 'image', 'created_at', 'audio_files', 'artist')
#         exclude = ('author',)

#     def create(self, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         album = Album.objects.create(author=user, **validated_data)
#         return album


#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['likes_count'] = instance.likes.count()
#         representation['rating_avg'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
#         return representation



# class AlbumSerializer(serializers.ModelSerializer):
#     audio_files = AudioFileSerializer(many=True, required=False)  # Указываем, что поле необязательное

#     class Meta:
#         model = Album
#         # fields = ('title', 'image', 'created_at', 'audio_files', 'artist')
#         exclude = ('author',)

#     def create(self, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         audio_files_data = validated_data.pop('audio_files', [])
#         album = Album.objects.create(author=user, **validated_data)
#         album.audio_files.set(audio_files_data)  # Исправление ошибки
#         return album

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['likes_count'] = instance.likes.count()
#         representation['rating_avg'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
#         return representation


# from .models import Album, AlbumItem



# class AlbumItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AlbumItem
#         fields = ['album', 'quantity']


# class AlbumSerializer(serializers.ModelSerializer):
#     items = AlbumItemSerializer(many=True)

#     class Meta:
#         model = Album
#         fields = ['id', 'created_at', 'items']

#     def create(self, validated_data):
#         albums = validated_data.pop('items')
#         validated_data['author'] = self.context['request'].user
#         album = super().create(validated_data)
#         album_items =  []
#         for album in albums:
#             album_items.append(AlbumItem(album=album, audiofile=album['audio_file'], quantity=album['quantity']))

#         AlbumItem.objects.bulk_create(album_items)
#         album.save()
#         return album