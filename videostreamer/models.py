from django.db import models
from django.utils import timezone
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    video = models.FileField(
    storage=VideoMediaCloudinaryStorage(), upload_to='video')
    # Stores the .m3u8 links for the video
    hls_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title
