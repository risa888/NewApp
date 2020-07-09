from rest_framework import serializers
from original.models import Post, Comments

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"




class CommentsSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    commenter = serializers.SerializerMethodField()
    pub_date = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        exclude = ['posted_id']

    
