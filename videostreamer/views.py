from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import VideoWriteSerializer, VideoListSerializer
from .models import Video
from rest_framework import status
from .utils import upload_video
from .permissions import IsCreator
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import transaction
import cloudinary.uploader
# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return VideoListSerializer
        return VideoWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permission() for permission in [AllowAny]]
        return [permission() for permission in [IsAuthenticated, IsCreator]]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                instance = serializer.save(creator=self.request.user)
                # This ensures the HLS upload happens only if the DB save succeeds
                upload_video(instance)
                return Response({
                    "message": "upload successful"
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = self.get_object()
        old_public_id = instance.video.name
        update_instance = serializer.save()

        if 'video' in serializer.validated_data:
            upload_video(update_instance)

            if old_public_id and old_public_id != update_instance.video.name:
                cloudinary.uploader.destroy(
                    old_public_id, resource_type="video")
