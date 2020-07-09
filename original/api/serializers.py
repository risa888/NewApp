from rest_framework import serializers
from original.models import Post, Comments

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"




class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
