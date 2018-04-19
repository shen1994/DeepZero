from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class MenuService(models.Model):
    author = models.ForeignKey(User, related_name="menu_service_author", \
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-created",)
        
    def __str__(self):
        return self.title
        
class MenuApplication(models.Model):
    author = models.ForeignKey(User, related_name="menu_application_author", \
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-created",)
        
    def __str__(self):
        return self.title
        
class MenuMessage(models.Model):
    author = models.ForeignKey(User, related_name="menu_message_author", \
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-created",)
        
    def __str__(self):
        return self.title
    
