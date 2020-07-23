from django.conf.urls import url
from django.urls import path, include

from original.api import views as ov
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', ov.PostViewSet)
router.register(r'comments', ov.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path("post/<slug:slug>/comment/", 
    #      ov.CommentsCreateAPIView.as_view(),
    #      name="comment-create"),
   
]