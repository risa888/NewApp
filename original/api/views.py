from django.contrib.auth.models import User

from original.api.serializers import CommentsSerializer, PostSerializer
from original.api.permissions import IsAuthorOrReadOnly
from original.models import Comments, Post

from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated





class PostViewSet(viewsets. ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostLikeAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        
        post = get_object_or_404(Post, slug=slug)
        user = request.user

        post.likes.remove(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        
        post = get_object_or_404(Post, slug=slug)
        user = request.user

        post.likes.add(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsListCreateAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        posted_id = get_object_or_404(Post, slug=kwarg_slug)

        if posted_id.comments.filter(commenter=request_user).exists():
            raise ValidationError("You have already left a comment!")

        serializer.save(commenter=request_user, posted_id=posted_id)

class CommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comments.objects.filter(posted_id__slug=kwarg_slug).order_by("-pub_date")

class CommentsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an answer instance to it's author."""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer




    # def get_queryset(self):
    #     kwarg_slug = self.kwargs.get("slug")
    #     return Comments.objects.filter(post__slug=kwarg_slug).order_by("-published_date")





