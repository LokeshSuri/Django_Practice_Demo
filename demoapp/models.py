from django.db import models
from datetime import datetime

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    video=models.FileField(upload_to="media/")
    description=models.TextField()
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)
    def __self__(self):
        return self.title
