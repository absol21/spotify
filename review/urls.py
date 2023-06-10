from django.urls import path, include
from .views import CommentViewSet, RatingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)
# router.register('create_playlists', PlaylistListCreateViewSet)
# router.register('detail_playlists', PlaylistDetailViewSet)

urlpatterns = [
    path('', include(router.urls))
]