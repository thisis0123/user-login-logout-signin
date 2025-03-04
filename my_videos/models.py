from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200)
    embed_code= models.CharField(default='https://www.youtube.com/embed/yg2kgBL_s10?si=uRHzk0OH_dHU2w5S' ,max_length=200)
    video_thumbnail= models.ImageField(default='black_image.jpg')
    date=models.DateTimeField(auto_now_add=True)
