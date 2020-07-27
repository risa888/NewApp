from django.contrib.auth.models import User

from original.api.serializers import CommentsSerializer, PostSerializer
from original.api.permissions import IsAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from original.models import Comments, Post

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated





class PostViewSet(viewsets. ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentsListCreateAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        posted_id = get_object(Post, slug=kwarg_slug)

        if posted_id.comments.filter(commenter=request_user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(commenter=request_user, posted_id=posted_id)

class CommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comments.objects.filter(posted_id__slug=kwarg_slug).order_by("-pub_date")




    # def get_queryset(self):
    #     kwarg_slug = self.kwargs.get("slug")
    #     return Comments.objects.filter(post__slug=kwarg_slug).order_by("-published_date")





