# Generated by Django 3.1.4 on 2020-12-07 10:05

import apps.profiles.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.profiles.models.upload_avatar_image),
        ),
    ]
