from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet
router = routers.SimpleRouter()
router.register(r'', VideoViewSet)

urlpatterns = [
    # path("upload/", UploadVideoView.as_view(), name="upload"),
    # path("list-videos/", ListVideoView.as_view(), name="list"),
    # path("delete/<pk>/", DeleteVideoView.as_view(), name="delete"),
    path("", include(router.urls))
]
