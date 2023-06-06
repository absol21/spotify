# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import PostSerializer, CategorySerializer, Category, Post


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['title', 'created_at']
    ordering_fields = ['title']

