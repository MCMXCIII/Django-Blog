from django.shortcuts import render

#Reference the Post model from earlier
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_pub')

    show_posts = {'posts' : posts}

    return render(request, 'blog/index.html', show_posts)

