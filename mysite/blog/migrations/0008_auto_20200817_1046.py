# Generated by Django 3.0.8 on 2020-08-17 09:46

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200817_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='post',
            name='processed_image',
            field=imagekit.models.fields.ProcessedImageField(default='post_images/default_post.jpg', upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='processed_profile_pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='profile_pics/default_profile.jpg', upload_to='profile_pics'),
        ),
    ]
