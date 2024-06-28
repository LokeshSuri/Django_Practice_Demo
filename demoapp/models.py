from django.db import models
from datetime import datetime
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    image=models.ImageField(upload_to="images/")
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class Blog(models.Model):
#     title=models.CharField(max_length=100)
#     image=models.ImageField(upload_to="images/")
#     video=models.FileField(upload_to="media/")
#     description=models.TextField()
#     author=models.CharField(max_length=100)
#     created_at=models.DateTimeField(default=datetime.now)
#     def __self__(self):
#         return self.title