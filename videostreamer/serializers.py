from rest_framework import serializers
from .models import Video
# from customuser.serializers import UserSerializer

class VideoUploadSerializer(serializers.ModelSerializer):  
    class Meta:
        model=Video
        fields=['id','title','description','video','creator','hls_url']
        read_only_fields = ['hls_url','creator']

class VideoListSerializer(serializers.ModelSerializer):
    creator=serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model=Video
        fields=['id','title','description','hls_url','uploaded_at','creator']
        read_only_fields=['hls_url']

class VideoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        
