from rest_framework import permissions, viewsets
from rest_framework.response import Response

from Post.models import Posts
from Post.permissions import IsAuthorOfPost
from Post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permission(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(), )

        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(PostViewSet, self).perform_create(serializer)

class UserPostViewSet(viewsets.ViewSet):
    queryset = Posts.objects.select_related('author').all()
    serializer_class = PostSerializer

    def list(self, request, user_username=None):
        queryset =  self.queryset.filter(author__username=user_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
