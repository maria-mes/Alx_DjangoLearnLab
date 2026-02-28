from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, UserViewSet

# Router for user actions (CRUD, follow/unfollow)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Authentication endpoints
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),

    # User routes (including follow/unfollow)
    path("", include(router.urls)),
]
