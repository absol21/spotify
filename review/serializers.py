from rest_framework.serializers import ModelSerializer,ValidationError,ReadOnlyField
from .models import Rating, Comment, Like

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
    
    
# class PlayListItemSerializer(ModelSerializer):
#     class Meta:
#         model = PlayListItem
#         fields = ('posts', 'quantity')

# class PlayListSerializer(ModelSerializer):
#     items = PlayListItemSerializer(many=True)

#     class Meta:
#         model = Playlist
#         fields = ('id', 'playlistitems', 'image')

#     def create(self, validated_data):
#         items = validated_data.pop('playlistitems')
#         validated_data['author'] = self.context['request'].user
#         playlist = super().create(validated_data)
#         playlistitems = []

#         image = 


#         for item in items:
#             playlistitems.append(PlayListItem(play=playlist, post=item['post'], quantity=item['quantity']))
        
#         PlayListItem.objects.bulk_create(playlistitems)
#         playlist.save()
#         return playlist