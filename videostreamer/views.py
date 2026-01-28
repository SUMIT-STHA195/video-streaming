from rest_framework import generics
from rest_framework.response import Response
from .serializers import VideoUploadSerializer, VideoListSerializer,VideoDeleteSerializer
from .models import Video
from rest_framework import status
from .utils import upload_video
from .permissions import IsCreator
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import transaction
# Create your views here.


class UploadVideoView(generics.CreateAPIView):
    serializer_class = VideoUploadSerializer
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                instance = serializer.save(creator=self.request.user)
                # For hls url
                upload_video(instance)
                return Response({
                    "message": "upload successful"
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    "error": str(e)
                },status=status.HTTP_400_BAD_REQUEST)


class ListVideoView(generics.ListAPIView):
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()
    permission_classes=[AllowAny]

class DeleteVideoView(generics.DestroyAPIView):
    serializer_class=VideoDeleteSerializer
    permission_classes=[IsAuthenticated,IsCreator]

    def get_queryset(self):
        return Video.objects.filter(creator=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message":"Video has been deleted"
        },status=status.HTTP_200_OK)
        



