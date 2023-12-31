from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    def __str__(self) -> str:
        return self.title
    
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)