# Generated by Django 3.0.8 on 2020-08-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200828_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]