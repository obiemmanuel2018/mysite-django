# Generated by Django 3.0.8 on 2020-08-17 11:00

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200817_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='processed_image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='post_images'),
        ),
    ]
