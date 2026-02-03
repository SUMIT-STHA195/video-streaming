from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
from django.dispatch import receiver
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
import cloudinary.uploader
from base_utils.models import BaseModel
# Create your models here.
# class BaseTracking(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     creator = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="creator")

#     class Meta:
#         abstract = True


class Video(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    video = models.FileField(
        storage=VideoMediaCloudinaryStorage(), upload_to='video')
    # Stores the .m3u8 links for the video
    hls_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Video)
def delete_video_file(sender, instance, **kwargs):
    if instance.video:
        public_id = instance.video.name
        cloudinary.uploader.destroy(public_id, resource_type="video")
