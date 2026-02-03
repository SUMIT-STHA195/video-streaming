from rest_framework import serializers

from customuser.serializers import UserSerializer
from .models import Video


class VideoWriteSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(required=False)
    # video = serializers.FileField(required=False)

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video',
                  'creator', 'hls_url', 'created_at', 'updated_at']
        read_only_fields = ['hls_url', 'creator']

    def get_creator(self, obj):
        return UserSerializer(instance=obj.created_by).data
