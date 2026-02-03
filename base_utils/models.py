from django.db import models
from django.conf import settings
from crum import get_current_user
# Create your models here.


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimestampModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='%(class)s_updated_by')

    class Meta:
        abstract = True
        ordering = ['-updated_at']

    def save(self, *args, **kwargs):
        user = get_current_user()
        import ipdb
        ipdb.set_trace()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(BaseModel, self).save(*args, **kwargs)
