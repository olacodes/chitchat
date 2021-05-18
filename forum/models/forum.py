import uuid
from django.db import models
from django.conf import settings


class Forum(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255, null=False)
  description = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
