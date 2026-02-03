from django.urls import path, include
from rest_framework import routers
from .views import UserVideoViewSet, VideoView
router = routers.SimpleRouter()
router.register(r'', UserVideoViewSet, basename='video')

urlpatterns = [
    # path("upload/", UploadVideoView.as_view(), name="upload"),
    # path("list-videos/", ListVideoView.as_view(), name="list"),
    # path("delete/<pk>/", DeleteVideoView.as_view(), name="delete"),
    path("",VideoView.as_view(),name="all-video"),
    path("user/", include(router.urls),name="user-video")
]
