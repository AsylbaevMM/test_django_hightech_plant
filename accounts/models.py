import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return reverse('accounts:user_detail',
                       args=[self.id])
# Create your models here.
