import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return None
# Create your models here.
