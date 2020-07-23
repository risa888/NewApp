from rest_framework import serializers
from original.models import Post, Comments




class CommentsSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    
    commenter = serializers.StringRelatedField(read_only=True)
    # pub_date = serializers.SerializerMethodField(read_only=True)
    post_slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comments
        exclude = ['posted_id']

    # def get_post_slug(self, instance):
    #     return instance.post_slug

    # def get_comment(self,instance):
    #     return instance.comment()





class PostSerializer(serializers.ModelSerializer):
    follow_count = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)


    class Meta:
        model = Post
        exclude = ['likes','follow']


    def get_follow_count(self, instance):
        return instance.follow.count()

    def get_likes_count(self, instance):
        return instance.likes.count()







    
