from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ProjectForm

from .models import Event

# Create your views here.


def index(request):
    events = Event.objects.filter().order_by('start')
    return render(request, 'blog/index.html', {'events': events})

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