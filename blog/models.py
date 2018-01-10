from django.db import models
from django.utils import timezone

# Create your models here.
# New models here
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Title: {}, ID: {}>'.format(self.title, self.id)
