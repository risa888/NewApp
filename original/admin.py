from django.contrib import admin
from.models import UserDetail, Post, Comments, Favorites, Follow, Tags

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Favorites)
admin.site.register(Follow)
admin.site.register(Tags)
