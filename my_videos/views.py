from django.shortcuts import render, redirect
from .models import Video

# Create your views here.
def goto_videos(request):
    videos= Video.objects.all()

    return render(request,'my_videos/videos.html', {'videos':videos})