# Generated by Django 3.0.8 on 2020-08-18 20:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20200817_1245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRegistration',
            new_name='UserProfileInfo',
        ),
    ]
