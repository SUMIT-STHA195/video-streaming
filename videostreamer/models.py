from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
from django.dispatch import receiver
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
import cloudinary.uploader
# Create your models here.
User=get_user_model()

class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    video = models.FileField(
    storage=VideoMediaCloudinaryStorage(), upload_to='video')
    # Stores the .m3u8 links for the video
    hls_url = models.URLField(blank=True, null=True)
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

@receiver(post_delete,sender=Video)
def delete_video_file(sender,instance,**kwargs):
    if instance.video:
        import ipdb; ipdb.set_trace()
        public_id=instance.video.name
        cloudinary.uploader.destroy(public_id,resource_type="video")

