# Generated by Django 3.0.8 on 2020-08-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200817_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default_post.jpg', upload_to='post_images'),
        ),
    ]
