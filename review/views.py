from .serializers import RatingSerializer
from .models import Rating
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsAuthorOrReadOnly


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update','destroy']:
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

    
class RatingViewSet(PermissionMixin,ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
