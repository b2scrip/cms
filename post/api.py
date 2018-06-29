from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostMixin(object):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostList(PostMixin, ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(PostMixin, RetrieveUpdateDestroyAPIView):
    pass
