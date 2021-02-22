import uuid
from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, null=False)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title


class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.post