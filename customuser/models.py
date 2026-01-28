from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_creator=models.BooleanField(default=False)
    REQUIRED_FIELDS=['first_name','last_name','email']
    def __str__(self):
        return f"{self.get_full_name()}-----{self.get_username()}"
