# Generated by Django 4.2.19 on 2025-03-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_videos', '0002_remove_video_videofile_video_video_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_image',
            new_name='video_thumbnail',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_link',
        ),
        migrations.AddField(
            model_name='video',
            name='embed_code',
            field=models.CharField(default='https://www.youtube.com/embed/yg2kgBL_s10?si=uRHzk0OH_dHU2w5S', max_length=200),
        ),
    ]
