from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import UserForm

from .models import Event

# Create your views here.


def index(request):
    events = Event.objects.filter().order_by('start')
    return render(request, 'blog/index.html', {'events': events})
