from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ProjectForm

from .models import Event, Post

# Create your views here.


def index(request):
    events = Event.objects.filter().order_by('start')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    return render(request, 'blog/index.html', {'events': events,'posts': posts})

def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/completed')
    else:
        form = ProjectForm()
    return render(request, 'blog/project.html', {'form': form})

def completed(request):
    return render(request, 'blog/completed.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})