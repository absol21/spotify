from rest_framework.serializers import ModelSerializer,ValidationError,ReadOnlyField
from .models import Rating,Comment,Playlist,Like

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                'Rating must be in range 1 - 6'
            )
        return rating

    def create(self,validated_data):
        user = self.context.get('request').user
        rating = Rating.objects.create(author=user,**validated_data)
        return rating
    

class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self,validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user,**validated_data)
        return comment


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    product = ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user 
        like = Like.objects.create(author=user,**validated_data)
        return like
    
    
class PlaylistSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    post = ReadOnlyField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user 
        playlist = Playlist.objects.create(author=user,**validated_data)
        return playlist


    