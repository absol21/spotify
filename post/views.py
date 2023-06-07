from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.core.exceptions import ValidationError
from PIL import Image

from .permissions import IsAdminOrActivePermission, IsOwnerPermission
from .serializers import PostSerializer, CategorySerializer, Category, Post

DEFAULT_IMAGE_PATH ='spotify/media/image/default_image/default_music_image.jpg'
IMAGE_MAX_SIZE = 10 * 1024 * 1024

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def validate_image(image_file):
    if image_file.size > IMAGE_MAX_SIZE:
        raise ValidationError('Image size exceeds the maximum limit.')

def open_image(image_file):
    if image_file:
        try:
            image = Image.open(image_file)
            return image
        except Exception:
            raise FileNotFoundError('Image file not found.')
    else:
        return None

def open_default_image():
    try:
        image = Image.open(DEFAULT_IMAGE_PATH)
        return image
    except Exception:
        raise FileNotFoundError('Default image file not found.')


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'created_at']
    ordering_fields = ['title']

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'partial_update']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            self.permission_classes = [IsAdminOrActivePermission]
        elif self.action in ['list', 'retrive']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @action(['POST'], detail=True)
    def process_image(self, request, pk=None):
        image_file = request.FILES.get('image')
    
        if image_file:
            validate_image(image_file)
            image = open_image(image_file)
        else:
            image = open_default_image()
            return Response('Image processed successfully.')

