from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrActivePermission, IsOwnerPermission
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from review.serializers import LikeSerializer#,PlaylistSerializer
from review.models import Like#,Playlist

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'created_at']
    ordering_fields = ['title']


    @action(methods=['POST'],detail=True)
    def like(self,request,pk=None):
        post = self.get_object()
        author = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(post=post,author=author)
                like.delete()
                message = 'disliked'
            except Like.DoesNotExist:
                Like.objects.create(post=post,author=author)
                message = 'liked'
            return Response(message,status=200)
        
    # @action(methods=['POST'],detail=True)
    # def playlist(self,request,pk=None):
    #     post = self.get_object()
    #     author = request.user
    #     serializer = PlaylistSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         try:
    #             playlist = Playlist.objects.get(post=post,author=author)
    #             playlist.delete()
    #             message = f'deleted from {self.playlist.title}'
    #         except Playlist.DoesNotExist:
    #             Playlist.objects.create(post=post,author=author)
    #             message = f'added to {self.playlist.title}'
    #         return Response(message,status=200)

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'partial_update']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            self.permission_classes = [IsAdminOrActivePermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()