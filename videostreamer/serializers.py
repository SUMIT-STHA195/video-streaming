from rest_framework import serializers
from .models import Video

class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=['id','title','description','video','hls_url']
        read_only_fields = ['hls_url']

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=['id','title','description','hls_url','uploaded_at']
        read_only_fields=['hls_url']
        # order_by=['-uploaded_at']
