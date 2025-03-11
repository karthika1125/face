from django.db import models


class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message from{self.name} ({self.email})"
 
from django.db import models
import os

class imageupload(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return os.path.basename(self.image.name)  # Get the base name of the uploaded image file


 


# Create your models here.
