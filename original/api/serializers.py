from rest_framework import serializers
from original.models import Post, Comments




class CommentsSerializer(serializers.ModelSerializer):
    
    commenter = serializers.StringRelatedField(read_only=True)
    pub_date = serializers.SerializerMethodField()
    post_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        exclude = ['posted_id']

    def get_pub_date(self, instance):
        return instance.pub_date.strftime("%y/%m/%d %H:%M")

    def get_post_slug(self, instance):
        return instance.posted_id.slug

    




class PostSerializer(serializers.ModelSerializer):
    follow_count = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    published_date = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ['likes','follow']

    
    def get_published_date(self, instance):
        return instance.pub_date.strftime("%y/%m/%d %H:%M")

    def get_comments_count(self, instance):
        return instance.comments.count()


    def get_follow_count(self, instance):
        return instance.follow.count()

    def get_likes_count(self, instance):
        return instance.likes.count()
    
    def user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()


class PostLikeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    user_has_commented = serializers.SerializerMethodField()


    def get_likes_count(self, instance):
        return instance.likes.count()

    def user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()



    class Meta:
        model = Post
        fields = ['likes','follow']







    
