# Generated by Django 4.2.13 on 2024-06-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_remove_post_image_height_remove_post_width_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]