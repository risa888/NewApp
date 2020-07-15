from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liker',blank=True)
    follow = models.ManyToManyField(User, related_name='follower')
    published_date = models.DateTimeField(auto_now_add=True)
    # tag_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.caption

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='commenter')
    posted_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.commenter)


class Favorites(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, \
                              related_name='favorite_post')
    favorite_ppl = models.ForeignKey(User, on_delete=models.CASCADE,)



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)


class Tags(models.Model):
    tag_name = models.ManyToManyField(Post)