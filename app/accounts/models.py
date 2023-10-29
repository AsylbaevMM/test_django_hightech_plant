import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(
        ("active"),
        default=False,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )
    email = models.EmailField(("email address"), blank=False, unique=True)

    def get_absolute_url(self):
        return reverse('accounts:user_detail',
                       args=[self.id])
# Create your models here.
