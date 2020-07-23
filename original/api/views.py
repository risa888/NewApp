from django.contrib.auth.models import User

from original.api.serializers import CommentsSerializer, PostSerializer
from original.api.permissions import IsAuthorOrReadOnly
from original.models import Comments, Post

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated





class PostViewSet(viewsets. ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    def post_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentsListCreateAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.commenter
        kwarg_slug = self.kwargs.get('slug')
        question = get_object(Post, slug=kwarg_slug)

    def get_queryset(self):
       return Comments.objects.all()


# class CommentsViewSet(viewsets. ModelViewSet):
#     queryset = Comments.objects.all()
#     lookup_field = 'slug'
    # serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]




