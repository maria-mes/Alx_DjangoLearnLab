from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, UserViewSet, FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),

    # Follow/unfollow using GenericAPIView
    path("users/<int:pk>/followuser/", FollowUserView.as_view(), name="followuser"),
    path("users/<int:pk>/unfollowuser/", UnfollowUserView.as_view(), name="unfollowuser"),

    path("", include(router.urls)),
]
