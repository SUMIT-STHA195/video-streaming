from django.urls import path
from .views import UploadVideoView,ListVideoView
urlpatterns=[
    path("upload/",UploadVideoView.as_view(),name="upload"),
    path("list-videos/",ListVideoView.as_view(),name="list")
]