from rest_framework import serializers
from original.models import Post, Comments




class CommentsSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField(read_only=True)
    commenter = serializers.StringRelatedField(read_only=True)
    pub_date = serializers.SerializerMethodField(read_only=True)
    post_slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comments
        exclude = ['posted_id']

    def get_post_slug(self, instance):
        return instance.post_slug





class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_comments_count(self, instance):
        return instance.comments_count()

    def get_likes_count(self, instance):
        return instance.likes_count()







    
