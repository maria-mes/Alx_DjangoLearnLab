from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

# Router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # CRUD routes for posts and comments
    path("", include(router.urls)),

    # Feed endpoint (Task 2)
    path("feed/", feed, name="feed"),
]
