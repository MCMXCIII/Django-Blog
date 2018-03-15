from django.db import models
from django.utils import timezone

#new models forms.


# Create your models here.
# New models here
# Post Model for Blog not Tube
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Title: {}, ID: {}>'.format(self.title, self.id)
#For tube posting videos from admin console.
class Video(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique = True,help_text="Url slugs")
    video_posts = models.TextField()
    date_pub = models.DateTimeField(default=timezone.now)
    allow_comments = models.BooleanField(default=False)



    def __str__(self):
        return '<ID: {}'.format(self.id)

#For Uploading stuff
class Files(models.Model):
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
