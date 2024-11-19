from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RegisterUserView, LoginUserView, CommunityPostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'community', CommunityPostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]
