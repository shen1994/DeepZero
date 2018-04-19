from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class TextChat(models.Model):
    user = models.ForeignKey(User, related_name="text_chat", \
                             on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-created",)