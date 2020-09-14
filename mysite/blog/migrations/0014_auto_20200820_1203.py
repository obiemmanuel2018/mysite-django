# Generated by Django 3.0.8 on 2020-08-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200818_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_profile_img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfileInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.TextField(null=True),
        ),
    ]
