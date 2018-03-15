#Remeber that these functions have to be impoted, check docs!
from django.shortcuts import render
from django.shortcuts import redirect

#Reference the Post model from earlier
from .models import Post
from .models import Video
from .forms import FileForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_pub')

    show_posts = {'posts' : posts}

    return render(request, 'blog/index.html', show_posts)

#Views for tube extension
def tube(request):
    videos = Video.objects.order_by('-date_pub')

    show_videos = {'videos' : videos}

    return render(request, 'blog/tube.html', show_videos)


#This will be moved to another view to merga this with a page.
def model_form_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tube')
    else:
        form = FileForm()
    return render(request, 'blog/model_form_upload.html', {
        'form': form
    })


