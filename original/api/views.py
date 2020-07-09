from django.contrib.auth.models import User

from original.api.serializers import PostSerializer
from original.api.permissions import IsAuthorOrReadOnly
from original.models import Post

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets. ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    # def post_create(self, serializer):
    #     serializer.save(author=self.request.user)

# class CommentsCreateAPIView(generics.CreateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
#     permission_classes = [IsAuthenticated]





