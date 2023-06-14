from rest_framework.serializers import ModelSerializer,ValidationError,ReadOnlyField
from .models import Rating, Like

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                'Rating must be in range 1 - 5'
            )
        return rating

    def create(self,validated_data):
        user = self.context.get('request').user
        rating = Rating.objects.create(author=user,**validated_data)
        return rating
    

class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    album = ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user 
        like = Like.objects.create(author=user,**validated_data)
        return like 