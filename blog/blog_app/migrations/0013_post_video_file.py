# Generated by Django 4.2.13 on 2024-06-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
