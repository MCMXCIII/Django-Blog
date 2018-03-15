from django.contrib import admin

from .models import Post
from .models import Video
# Register your models here.
#  new Models

admin.site.register(Post)
admin.site.register(Video)

