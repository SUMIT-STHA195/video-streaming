
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from .serializers import VideoUploadSerializer,VideoListSerializer
from .models import Video
from rest_framework import status
from .utils import upload_video
# Create your views here.


class UploadVideoView(CreateAPIView):
    serializer_class = VideoUploadSerializer
    queryset = Video.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        # For hls url
        try:
            upload_video(instance)
            return Response({
                "message": "upload successful"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    "error": str(e)
                },status=status.HTTP_400_BAD_REQUEST)


class ListVideoView(ListAPIView):
    serializer_class=VideoListSerializer
    queryset=Video.objects.all()
    
