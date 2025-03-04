from django.shortcuts import render, redirect
from .models import Video
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='users:signin')
def goto_videos(request):
    videos= Video.objects.all().order_by('-date')
    return render(request,'my_videos/videos.html', {'videos':videos})