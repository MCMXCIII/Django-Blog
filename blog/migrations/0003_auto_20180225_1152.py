# Generated by Django 2.0 on 2018-02-25 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='tags',
            new_name='video_posts',
        ),
    ]
