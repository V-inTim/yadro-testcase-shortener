from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    original_link = models.CharField(max_length=500)
    short_code = models.CharField(max_length=40, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    clicks = models.IntegerField(default=0)

    @property
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(days=1)
