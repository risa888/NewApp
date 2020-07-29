from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="post_author")

    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    title = models.CharField(max_length=50)
    caption = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,
                                   related_name="liker")

    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,
                                    related_name="follow_ppl")

    published_date = models.DateTimeField(auto_now_add=True)
    # tag_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.caption)

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name="commenters")

    posted_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.commenter)


class Favorites(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, \
                              related_name='favorite_post')
    favorite_ppl = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name="favorite")




class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name="follower")



class Tags(models.Model):
    tag_name = models.ManyToManyField(Post)