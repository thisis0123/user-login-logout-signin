from django.urls import path
from . import views

app_name= 'my_videos'

urlpatterns = [
    path('', views.goto_videos, name='videos')
]
