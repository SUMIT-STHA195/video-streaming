from django.db import models
from django_currentuser.db.models import CurrentUserField
# Create your models here.


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimestampModel):
    created_by = CurrentUserField(related_name="%(class)s_created_by")
    updated_by = CurrentUserField(
        on_update=True, related_name="%(class)s_updated_by")

    class Meta:
        abstract = True
        ordering = ['-updated_at']
