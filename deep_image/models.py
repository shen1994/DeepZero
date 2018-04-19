from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImageImage(models.Model):
    user = models.ForeignKey(User, related_name="images",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    url = models.URLField()
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
        
class ImageRetrieval(models.Model):
    user = models.ForeignKey(User, related_name="images_retrieval",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    status = models.BooleanField()
    created = models.DateField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title    
    