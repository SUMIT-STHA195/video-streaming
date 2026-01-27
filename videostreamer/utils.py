from cloudinary import uploader
def upload_video(instance):
    upload_data = uploader.explicit(
                public_id=instance.video.name,
                type="upload",
                resource_type="video",
                eager=[
                    {
                        "streaming_profile": "full_hd",
                        "format": "m3u8"
                    }
                ],
                eager_async=True
            )
    if 'eager' in upload_data:
                instance.hls_url = upload_data['eager'][0]['secure_url']
                instance.save()