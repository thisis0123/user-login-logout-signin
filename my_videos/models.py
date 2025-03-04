from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200)
    videofile= models.FileField(upload_to='video/%y')
    date=models.DateTimeField(auto_now_add=True)
